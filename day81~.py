def load_study():
    study = {}

    try:
        with open("study.txt","r",encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    subject, time = line.strip(",")
                    study[subject] = int(time)

                except ValueError:
                    print("読み込めないデータがあります")

    except FileNotFoundError:
        print("study.txtがありません")

    return study

study = load_study()
print("===勉強記録===")

for subject, time in study.items():
    print(subject,":", time ,"時間")
    