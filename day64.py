study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
def show_menu():
    print("\n===勉強記録アプリ===")
    print("1: 勉強記録を見る")
    print("2: 合計時間を見る")
    print("3: 平均時間を見る")
    print("4: 終了")

def show_study():
    for subject, time in study.items():
        print(subject,":",time, "時間")
def show_total():
    print("合計:",sum(study.values()),"時間")
def show_average():
    average = sum(study.values()) / len(study)
    print("平均:",average,"時間")

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
        print("終了します")
        break
    else:
        print("番号が違います")