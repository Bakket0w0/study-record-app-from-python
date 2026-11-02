"""ブラウザで使える勉強記録アプリ（Streamlit版）。"""

from __future__ import annotations

import csv
import io
import sqlite3
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import streamlit as st
import xlsxwriter

try:
    from supabase import Client, create_client
except ImportError:
    Client = Any
    create_client = None


DB_PATH = Path(__file__).with_name("study_records.db")


@st.cache_resource
def get_supabase_client() -> Client | None:
    """公開版で使うクラウド保存先に接続する。設定がない時はPC保存版を使う。"""
    if create_client is None:
        return None

    try:
        supabase_url = st.secrets["SUPABASE_URL"]
        supabase_key = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]
    except (KeyError, FileNotFoundError):
        return None

    return create_client(supabase_url, supabase_key)


def using_cloud_database() -> bool:
    """Supabaseが設定済みかどうかを返す。"""
    return get_supabase_client() is not None


def initialize_database() -> None:
    """PC内に勉強記録用のデータベースを用意する。"""
    if using_cloud_database():
        return

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                study_date TEXT NOT NULL,
                user_name TEXT NOT NULL,
                subject TEXT NOT NULL,
                hours INTEGER NOT NULL CHECK(hours > 0)
            )
            """
        )

        columns = {
            row[1] for row in connection.execute("PRAGMA table_info(records)")
        }
        if "user_name" not in columns:
            connection.execute(
                "ALTER TABLE records ADD COLUMN user_name TEXT NOT NULL DEFAULT '未設定'"
            )


def add_record(study_date: date, user_name: str, subject: str, hours: int) -> None:
    """入力された勉強記録をすぐに保存する。"""
    supabase = get_supabase_client()
    if supabase is not None:
        supabase.table("study_records").insert(
            {
                "study_date": study_date.isoformat(),
                "user_name": user_name,
                "subject": subject,
                "hours": hours,
            }
        ).execute()
        return

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            INSERT INTO records (study_date, user_name, subject, hours)
            VALUES (?, ?, ?, ?)
            """,
            (study_date.isoformat(), user_name, subject, hours),
        )


def migrate_legacy_session_records() -> None:
    """旧版でブラウザに一時保存されていた記録を一度だけ引き継ぐ。"""
    if st.session_state.get("legacy_records_migrated"):
        return

    for record in st.session_state.get("records", []):
        add_record(
            date.fromisoformat(record["date"]),
            str(record.get("user_name", "未設定")),
            str(record["subject"]),
            int(record["hours"]),
        )

    st.session_state.legacy_records_migrated = True


def load_records() -> list[dict[str, str | int]]:
    """保存済みの全記録を新しい順に読み込む。"""
    supabase = get_supabase_client()
    if supabase is not None:
        response = (
            supabase.table("study_records")
            .select("id, study_date, user_name, subject, hours")
            .order("study_date", desc=True)
            .order("id", desc=True)
            .execute()
        )
        return [
            {
                "id": int(row["id"]),
                "date": str(row["study_date"]),
                "user_name": str(row["user_name"]),
                "subject": str(row["subject"]),
                "hours": int(row["hours"]),
            }
            for row in response.data
        ]

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT id, study_date, user_name, subject, hours
            FROM records
            ORDER BY study_date DESC, id DESC
            """
        ).fetchall()

    return [
        {
            "id": row["id"],
            "date": row["study_date"],
            "user_name": row["user_name"],
            "subject": row["subject"],
            "hours": row["hours"],
        }
        for row in rows
    ]


def records_as_csv(records: list[dict[str, str | int]]) -> str:
    """記録をダウンロードできるCSV文字列にする。"""
    output = io.StringIO()
    writer = csv.DictWriter(
        output, fieldnames=["date", "user_name", "subject", "hours"]
    )
    writer.writeheader()
    writer.writerows(
        {
            "date": record["date"],
            "user_name": record["user_name"],
            "subject": record["subject"],
            "hours": record["hours"],
        }
        for record in records
    )
    return output.getvalue()


def records_as_excel(records: list[dict[str, str | int]]) -> bytes:
    """記録を整えたExcelファイルにしてダウンロードできるようにする。"""
    output = io.BytesIO()

    with xlsxwriter.Workbook(output, {"in_memory": True}) as workbook:
        worksheet = workbook.add_worksheet("勉強記録")
        header_format = workbook.add_format(
            {"bold": True, "bg_color": "#E8F1FF", "border": 1}
        )
        date_format = workbook.add_format({"num_format": "yyyy-mm-dd"})
        hours_format = workbook.add_format({"num_format": '0"時間"'})

        worksheet.write_row(
            0, 0, ["日付", "利用者", "教科", "勉強時間"], header_format
        )

        for row, record in enumerate(records, start=1):
            worksheet.write_datetime(
                row,
                0,
                date.fromisoformat(str(record["date"])),
                date_format,
            )
            worksheet.write(row, 1, record["user_name"])
            worksheet.write(row, 2, record["subject"])
            worksheet.write_number(row, 3, int(record["hours"]), hours_format)

        worksheet.set_column("A:A", 14)
        worksheet.set_column("B:B", 18)
        worksheet.set_column("C:C", 18)
        worksheet.set_column("D:D", 14)
        worksheet.freeze_panes(1, 0)

    return output.getvalue()


def filtered_records(
    records: list[dict[str, str | int]],
    user_name: str,
    subject: str,
    selected_date: date | None,
    min_hours: int,
) -> list[dict[str, str | int]]:
    """指定した条件に合う記録だけを返す。"""
    results = []

    for record in records:
        if user_name and user_name not in str(record["user_name"]):
            continue
        if subject and subject not in str(record["subject"]):
            continue
        if selected_date and record["date"] != selected_date.isoformat():
            continue
        if int(record["hours"]) < min_hours:
            continue
        results.append(record)

    return sorted(results, key=lambda record: int(record["hours"]), reverse=True)


st.set_page_config(page_title="勉強記録アプリ", page_icon="📚", layout="centered")
initialize_database()
migrate_legacy_session_records()

st.title("📚 勉強記録アプリ")
if using_cloud_database():
    st.caption("みんなの記録をクラウドに自動保存します。")
else:
    st.caption("勉強時間を記録して、検索やランキングで振り返ろう。")

record_tab, search_tab, ranking_tab = st.tabs(["記録する", "検索する", "ランキング"])

with record_tab:
    st.subheader("今日の勉強を追加")

    with st.form("add_record", clear_on_submit=True):
        user_name = st.text_input("利用者名", placeholder="例：A01")
        subject = st.text_input("教科", placeholder="例：英語")
        hours = st.number_input("勉強時間（時間）", min_value=1, max_value=24, step=1)
        study_date = st.date_input("日付", value=date.today())
        submitted = st.form_submit_button("記録を追加")

    if submitted:
        if not user_name.strip() or not subject.strip():
            st.error("利用者名と教科を入力してください。")
        else:
            try:
                add_record(study_date, user_name.strip(), subject.strip(), int(hours))
            except Exception:
                st.error("保存に失敗しました。少し待ってから、もう一度追加してください。")
            else:
                st.success(
                    f"{user_name.strip()}さんの{subject.strip()}を{int(hours)}時間、保存しました！"
                )

    try:
        records = load_records()
    except Exception:
        st.error("記録の読み込みに失敗しました。少し待ってから再読み込みしてください。")
        records = []
    st.subheader("記録一覧")
    if not records:
        st.info("まだ記録がありません。上のフォームから追加してみよう！")
    else:
        st.dataframe(
            [
                {
                    "日付": record["date"],
                    "利用者": record["user_name"],
                    "教科": record["subject"],
                    "時間": f"{record['hours']}時間",
                }
                for record in records
            ],
            hide_index=True,
            use_container_width=True,
        )

        st.download_button(
            "記録をExcelでダウンロード",
            data=records_as_excel(records),
            file_name="study_records.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        st.download_button(
            "記録をCSVでダウンロード",
            data=records_as_csv(records),
            file_name="study_records.csv",
            mime="text/csv",
        )

try:
    records = load_records()
except Exception:
    records = []

with search_tab:
    st.subheader("条件を指定して検索")
    search_user_name = st.text_input("利用者名に含まれる文字", key="search_user_name")
    search_subject = st.text_input("教科名に含まれる文字", key="search_subject")
    search_date_enabled = st.checkbox("日付を指定する")
    search_date = st.date_input("日付", value=date.today(), disabled=not search_date_enabled)
    min_hours = st.number_input("何時間以上", min_value=0, max_value=24, step=1, key="min_hours")

    results = filtered_records(
        records,
        search_user_name.strip(),
        search_subject.strip(),
        search_date if search_date_enabled else None,
        int(min_hours),
    )

    st.write(f"検索結果：{len(results)}件")
    if results:
        st.dataframe(
            [
                {
                    "日付": record["date"],
                    "利用者": record["user_name"],
                    "教科": record["subject"],
                    "時間": f"{record['hours']}時間",
                }
                for record in results
            ],
            hide_index=True,
            use_container_width=True,
        )

with ranking_tab:
    st.subheader("教科別・勉強時間ランキング")

    totals = defaultdict(int)
    user_totals = defaultdict(int)
    for record in records:
        totals[str(record["subject"])] += int(record["hours"])
        user_totals[str(record["user_name"])] += int(record["hours"])

    ranking = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    if not ranking:
        st.info("記録を追加するとランキングが表示されます。")
    else:
        for rank, (subject, hours) in enumerate(ranking, start=1):
            st.write(f"**{rank}位：{subject}**　{hours}時間")

        st.subheader("利用者別・合計勉強時間")
        for user_name, hours in sorted(
            user_totals.items(), key=lambda item: item[1], reverse=True
        ):
            st.write(f"**{user_name}**　{hours}時間")

st.divider()
st.caption("記録はこのPC内に自動保存されます。バックアップにはExcelまたはCSVをダウンロードしてください。")
