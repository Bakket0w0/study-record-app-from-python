def load_study():
    study = {}
    try:
        with open("study.txt","r", encoding="utf-8") as file:
            for line in file:
                subject, time = line.strip().split(",")
                study[subject]= int(time)
    except FileNotFoundError:
        pass
    return study    
def save_study(study):
    with open("study.txt","w",encoding="utf-8") as file:
        for subject, time in study.items():
            file.write(subject + "," + str(time)+ "\n")

def show_study(study):
    for subject, time in study.items():
        print(subject, ":", time, "時間")
def add_subject(study):
    subject = input("教科:")
    try:
        time = int(input("勉強時間:"))
        study[subject] = time 
        print("追加しました！")
    except ValueError:
        print("数字を入力してください")
study = load_study()
while True:
    print("\n===勉強記録アプリ===")
    print("1: 表示")
    print("2: 追加")
    print("3: 保存")
    print("4: 終了")

    choice = input("番号")

    if choice =="1":
        show_study(study)
    elif choice =="2":
        add_subject(study)
    elif choice == "3":
        save_study(study)
        print("保存しました！")
    elif choice == "4":
        save_study(study)
        print("保存して終了します")
        break
    else:
        print("番号が違います")