def load_study():
    study = {}
    try:
        with open("study.txt", "r", encoding="utf-8") as file:
            for line in file:
                subject, time = line.strip().split(",")
                study[subject] = int(time)
    except FileNotFoundError:
        print("保存ファイルがありません。新しく開始します")
    return study

study = load_study()
print("現在の勉強記録")
for subject, time in study.items():
    print(subject, ":", time,"時間")