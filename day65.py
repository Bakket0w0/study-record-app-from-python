study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
def add_subject():
    subject = input("教科:")
    try:
        time = int(input("勉強時間:"))
        study[subject] = time
        print("追加しました！")
    except ValueError:
        print("数字を入力してください")

def show_study():
    for subject, time in study.items():
        print(subject, ":", time,"時間")

while True:
    print("\n=== 勉強記録アプリ ===")
    print("1: 表示")
    print("2: 追加")
    print("3: 終了")

    choice = input("番号")
    if choice == "1":
      show_study()
    elif choice == "2":
      add_subject()
    elif choice == "3":
      print("終了します")
      break
    else:
       print("番号が違います")
