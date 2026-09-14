study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

while True:

    print("\n=== 勉強記録アプリ ===")
    print("1:表示")
    print("2:追加")
    print("3:削除")
    print("4:更新")
    print("5:終了")

    choice = input("番号:")

    if choice == "1":

        for subject, time in study.items():
            print(subject, ":", time)

    elif choice == "2":

        subject = input("教科:")
        time = int(input("時間:"))

        study[subject] = time

    elif choice == "3":

        subject = input("削除:")

        if subject in study:
            del study[subject]

    elif choice == "4":

        subject = input("更新:")

        if subject in study:
            study[subject] = int(input("時間:"))

    elif choice == "5":

        print("終了")
        break

    else:
        print("番号が違います")