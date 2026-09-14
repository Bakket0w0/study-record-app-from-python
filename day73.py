study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}


def show_menu():

    print("\n=== 勉強記録アプリ ===")
    print("1: 勉強記録を見る")
    print("2: 教科を追加")
    print("3: 教科を削除")
    print("4: 勉強時間を更新")
    print("5: 合計時間")
    print("6: 平均時間")
    print("7: ランキング")
    print("8: 終了")


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

        print("数字を入力してください")


def delete_subject():

    subject = input("削除する教科:")

    if subject in study:

        del study[subject]

        print("削除しました！")

    else:

        print("その教科はありません")


def update_subject():

    subject = input("更新する教科:")

    if subject in study:

        try:

            time = int(input("新しい勉強時間:"))

            study[subject] = time

            print("更新しました！")

        except ValueError:

            print("数字を入力してください")

    else:

        print("その教科はありません")


def show_total():

    total = sum(study.values())

    print("合計:", total, "時間")


def show_average():

    if len(study) == 0:

        print("教科がありません")

    else:

        average = sum(study.values()) / len(study)

        print("平均:", average, "時間")


def show_ranking():

    ranking = sorted(
        study.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n=== 勉強時間ランキング ===")

    for number, (subject, time) in enumerate(ranking, start=1):

        print(number, "位:", subject, time, "時間")


while True:

    show_menu()

    choice = input("番号:")

    if choice == "1":

        show_study()

    elif choice == "2":

        add_subject()

    elif choice == "3":

        delete_subject()

    elif choice == "4":

        update_subject()

    elif choice == "5":

        show_total()

    elif choice == "6":

        show_average()

    elif choice == "7":

        show_ranking()

    elif choice == "8":

        print("終了します")
        break

    else:

        print("番号が違います")