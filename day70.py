study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_menu():
    print("\n===　勉強記録アプリ　===")
    print("1: 表示")
    print("2: 追加")
    print("3: 削除")
    print("4: 更新")
    print("5: 合計")
    print("6: 平均")
    print("7: 終了")

def show_study():
    for subject, time in study.items():
        print(subject,":", time, "時間")
def show_total():
    print("合計:", sum(study.values()),"時間")
def show_average():
    if len(study) == 0:
        print("教科がありません")
    else:
        print("平均:", sum(study.values())/ len(study), "時間")

while True:
    show_menu()
    choice = input("番号:")
    if choice == "1":
        show_study()
    elif choice =="5":
        show_total()
    elif choice =="6":
        show_average()
    elif choice == "7":
        print("終了します")
        break
    else:
        print("この機能はまだ作成中です")