study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_menu():
    print("1:勉強時間を見る")
    print("2:終了")
    print("3:合計時間を見る")

def show_study():
    print("【勉強記録】")
    for subject, time in study.items():
        print(subject,":", time,"時間")

def show_total():
    total = sum(study.values())
    print("合計", total,"時間です")

show_menu()

choice = input("番号を入力")

if choice == "1":
    show_study()

elif choice == "2":
    print("終了します")

elif choice == "3":
    show_total()

else:
    print("その番号はありません")