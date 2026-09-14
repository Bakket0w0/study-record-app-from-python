study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}


def show_study():

    print("\n--- 勉強記録 ---")

    for subject, time in study.items():
        print(subject, ":", time, "時間")


def add_subject():

    subject = input("教科:")

    try:

        time = int(input("勉強時間:"))

        study[subject] = time

        print("追加しました！")

    except ValueError:

        print("勉強時間には数字を入力してください")


def show_total():

    total = sum(study.values())

    print("合計:", total, "時間")


def show_average():

    if len(study) == 0:

        print("まだ教科がありません")

    else:

        average = sum(study.values()) / len(study)

        print("平均:", average, "時間")


while True:

    print("\n=== 勉強記録アプリ ===")
    print("1: 勉強記録を見る")
    print("2: 教科を追加する")
    print("3: 合計時間を見る")
    print("4: 平均時間を見る")
    print("5: 終了")

    choice = input("番号:")

    if choice == "1":

        show_study()

    elif choice == "2":

        add_subject()

    elif choice == "3":

        show_total()

    elif choice == "4":

        show_average()

    elif choice == "5":

        print("終了します")
        break

    else:

        print("番号が違います")