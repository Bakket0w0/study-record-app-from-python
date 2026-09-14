study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_menu():
    print("\n=== 勉強記録 ===")
    print("1:表示")
    print("2:合計")
    print("3:平均")
    print("4:終了")

def show_study():
    for subject, time in study.items():
        print(subject, ":", time)

def show_total():
    print(sum(study.values()))

def show_average():
    print(sum(study.values()) / len(study))

while True:

    show_menu()

    choice = input("番号:")

    if choice == "1":
        show_study()

    elif choice == "2":
        show_total()

    elif choice == "3":
        show_average()

    elif choice == "4":
        print("終了")
        break

    else:
        print("番号が違います