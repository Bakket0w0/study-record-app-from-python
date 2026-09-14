study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_study():
    for subject, time in study.items():
        print(subject,":", time,"時間")
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

while True:
    print("\n=== 勉強記録アプリ ===")
    print("1: 表示")
    print("2: 追加") 
    print("3: 削除")
    print("4: 更新")
    print("5: 終了")

    choice = input("番号:")
    if choice == "1":
        show_study()
    elif choice =="2":
        add_subject()
    elif choice == "3":
        delete_subject()
    elif choice == "4":
        update_subject()
    elif choice == "5":
        print("終了します")
        break
    else:
        print("番号が違います")    