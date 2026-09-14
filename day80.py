def load_study():
    study = {}

    try:
        with open("study.txt","r", encoding="utf-8") as file:
            for line in file:
                subject, time = line.strip().split(",")
                study[subject] = int(time)
    except FileNotFoundError:
        pass
    return study

def save_study(study):
    with open("study.txt", "w", encoding="utf-8") as file:
        for subject, time in study.items():
            file.write(subject + "," + str(time)+ "\n")

def show_study(study):
    print("\n--- 勉強記録 ---")
    for subject, time in study.items():
        print(subject, ":", time ,"時間")
def add_subejct(study):
    subject = input("教科:")
    try:
        time = int(input("勉強時間:"))
        study[subject] = time
        print("追加しました！")
    except ValueError:
        print("数字を入力してください")

def delete_subject(study):
    subject = input("削除する教科:")
    if subject in study:
        del study[subject]
        print("削除しました")
    else:
        print("その教科はありません")

def update_subject(study):
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

def show_total(study):
    print("合計:", sum(study.values()),"時間")

def show_average(study):
    if len(study) == 0:
        print("教科がありません")
    else:
        average = sum(study.values()) / len(study)
        print("平均:", average, "時間")

study = load_study()

while True:
    print("\n===勉強記録アプリ===")
    print("1:表示")
    print("2:追加")
    print("3:削除")
    print("4:更新")
    print("5:合計")
    print("6:平均")
    print("7:保存")
    print("8:終了")

    choice = input("番号:")

    if choice == "1":
        show_study(study)
    elif choice == "2":
        add_subejct(study)
    elif choice == "3":
        delete_subject(study)
    elif choice == "4":
        update_subject(study)
    elif choice == "5":
        show_total(study)
    elif choice == "6":
        show_average(study)
    elif choice == "7":
        save_study(study)
        print("保存しました！")
    elif choice == "8":
        save_study(study)
        print("保存して終了します")
        break
    else:
        print("番号が違います")