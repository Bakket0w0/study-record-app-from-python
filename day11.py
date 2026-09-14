study = {
    "数学": 3,
    "英語": 2
}

while True:

    print("1:記録を見る")
    print("2:終了")

    choice = input("選んでください:")

    if choice == "1":
        print("勉強記録")
        print(study)

    elif choice == "2":
        print("終了します")
        break