from datetime import datetime


class StudyRecord:

    def __init__(self, subject, time, date=None):
        self.subject = subject
        self.time = time
        self.date = date

    def show(self):
        if self.date is None:
            print(self.subject, ":", self.time, "時間")
        else:
            print(self.date, self.subject, ":", self.time, "時間")

    def add_time(self, time):
        self.time += time

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time


class StudyManager:

    def __init__(self):
        self.records = []

    # データを読み込む
    def load_data(self):

        self.records = []

        try:

            with open("study.txt", "r", encoding="utf-8") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    parts = line.split(",")

                    try:

                        if len(parts) == 3:

                            subject = parts[0]
                            time = int(parts[1])
                            date = parts[2]

                            record = StudyRecord(subject, time, date)
                            self.records.append(record)

                        elif len(parts) == 2:

                            # 昔のデータにも対応
                            subject = parts[0]
                            time = int(parts[1])

                            record = StudyRecord(subject, time)
                            self.records.append(record)

                    except ValueError:
                        print("読み込めないデータをスキップしました:", line)

        except FileNotFoundError:
            pass

    # データを保存する
    def save_data(self):

        with open("study.txt", "w", encoding="utf-8") as file:

            for record in self.records:

                if record.date is None:

                    # 古いデータも日付付きにする
                    today = datetime.now().strftime("%Y-%m-%d")

                    file.write(
                        record.subject + "," +
                        str(record.time) + "," +
                        today + "\n"
                    )

                else:

                    file.write(
                        record.subject + "," +
                        str(record.time) + "," +
                        record.date + "\n"
                    )

    # 教科を追加
    def add_subject(self, subject, time):

        for record in self.records:

            if record.subject == subject and record.date is None:
                record.add_time(time)
                return

        record = StudyRecord(subject, time)
        self.records.append(record)

    # 今日の勉強を追加
    def add_today(self, subject, time):

        today = datetime.now().strftime("%Y-%m-%d")

        record = StudyRecord(subject, time, today)
        self.records.append(record)

    # 教科を削除
    def delete_subject(self, subject):

        for record in self.records:

            if record.subject == subject:

                self.records.remove(record)
                return True

        return False

    # 勉強時間を変更
    def change_time(self, subject, time):

        for record in self.records:

            if record.subject == subject:

                record.change_time(time)
                return True

        return False

    # 全部表示
    def show_all(self):

        if len(self.records) == 0:
            print("勉強記録がありません")
            return

        for record in self.records:
            record.show()

    # ランキング
    def show_ranking(self):

        if len(self.records) == 0:
            print("勉強記録がありません")
            return

        ranking = sorted(
            self.records,
            key=lambda record: record.get_time(),
            reverse=True
        )

        print()
        print("=== 勉強時間ランキング ===")

        for rank, record in enumerate(ranking, start=1):

            print(
                rank,
                "位",
                record.subject,
                ":",
                record.get_time(),
                "時間"
            )

    # 統計
    def show_statistics(self):

        if len(self.records) == 0:
            print("勉強記録がありません")
            return

        total = 0

        for record in self.records:
            total += record.get_time()

        average = total / len(self.records)

        best = self.records[0]

        for record in self.records:

            if record.get_time() > best.get_time():
                best = record
                print()
                print("=== 勉強統計 ===")
                print("合計勉強時間:", total, "時間")
                print("平均勉強時間:", average, "時間")
                print("一番勉強した教科:", best.subject)

    #勉強履歴
    def show_history(self):
        print()
        print("=== 勉強履歴 ===")
        for record in self.records:
            if record.date is not None:
                print(
                    record.date,
                    record.subject,
                    ":",
                    record.time,
                    "時間"
                )

    #日付別勉強時間
    def show_daily_total(self):
        print()
        print("=== 日付別勉強時間 ===")

        daily_totals = {}

        for record in self.records:
            if record.date is not None:
                if record.date not in daily_totals:
                    daily_totals[record.date] = 0

                daily_totals[record.date] += record.time

        for date,total in daily_totals.items():
            print(date, ",", total, "時間")

    #日付指定履歴
    def show_by_date(self,date):
        print()
        print(date,"の勉強記録")
        found = False

        for record in self.records:
            if record.date == date:
                print(record.subject, ":", record.time, "時間")
                found = True

        if not found:
            print("この日の勉強記録はありません")

    #教科検索機能
    def search_subject(self,subject):
        found = False

        print()
        print("=== 検索結果 ===")
        for record in self.records:
            if record.subject == subject:
                if record.date is None:
                    print(record.subject, ":", record.time, "時間")
                else:
                    print(record.date, record.subject, ":", record.time, "時間")

                found = True
        if found == False:
            print(subject,"の記録はありません")
                


# アプリ開始
manager = StudyManager()

# 保存されているデータを読み込む
manager.load_data()


while True:

    print()
    print("=== 勉強記録アプリ ===")
    print("1. 教科を追加")
    print("2. 教科を削除")
    print("3. 勉強記録を表示")
    print("4. 勉強時間を変更")
    print("5. ランキング")
    print("6. 勉強統計")
    print("7. 今日の勉強を追加")
    print("8. 勉強履歴を見る")
    print("9. 日付を指定して見る")
    print("10. 日付別勉強時間")
    print("11. 保存して終了")
    print("12. 教科を検索")

    choice = input("選択してください: ")

    # 教科を追加
    if choice == "1":

        subject = input("教科を入力してください: ")
        time = int(input("勉強時間を入力してください: "))

        manager.add_subject(subject, time)

        print("追加しました！")

    # 教科を削除
    elif choice == "2":

        subject = input("削除する教科を入力してください: ")

        if manager.delete_subject(subject):
            print(subject, "を削除しました")
        else:
            print(subject, "は登録されていません")

    # 表示
    elif choice == "3":

        print()
        print("=== 現在の勉強記録 ===")

        manager.show_all()

    # 勉強時間変更
    elif choice == "4":

        subject = input("変更する教科を入力してください: ")
        time = int(input("新しい勉強時間を入力してください: "))

        if manager.change_time(subject, time):
            print(subject, "の勉強時間を変更しました")
        else:
            print(subject, "は登録されていません")

    # ランキング
    elif choice == "5":

        manager.show_ranking()

    # 統計
    elif choice == "6":

        manager.show_statistics()

    # 今日の勉強
    elif choice == "7":

        subject = input("今日勉強した教科を入力してください: ")
        time = int(input("勉強時間を入力してください: "))

        manager.add_today(subject, time)

        print("今日の勉強を追加しました！")

    #勉強履歴を見る
    elif choice == "8":
        manager.show_history()

    #日付指定
    elif choice == "9":
        date = input("みたい日付を入力してください(YYYY-MM-DD):")
        manager.show_by_date(date)

    #日付別勉強時間
    elif choice == "10":
        manager.show_daily_total()
        
    # 保存して終了
    elif choice == "11":

        manager.save_data()

        print("データを保存しました")
        print("アプリを終了します")

        break

    #教科検索機能
    elif choice == "12":
        subject = input("検索する教科を入力してください:")

        manager.search_subject(subject)

    else:

        print("1〜12を入力してください")