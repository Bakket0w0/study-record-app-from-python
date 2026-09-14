study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_menu():
    print("1:勉強記録を見る")
    print("2:終了")

def show_study():
    print("📗勉強記録")
    for subject, time in study.items():
        print(subject,":",time,"時間")

show_menu()

choice = input("番号を入力:")

if choice == "1":
    show_study()

elif choice == "2":
    print("終了します")

else:
    print("その番号はありません")
          