def load_study():

    study = {}

    try:

        with open("study.txt", "r", encoding="utf-8") as file:

            for line in file:

                subject, time = line.strip().split(",")

                study[subject] = int(time)

    except FileNotFoundError:

        print("保存ファイルがありません。")

    return study


def save_study(study):

    with open("study.txt", "w", encoding="utf-8") as file:

        for subject, time in study.items():

            file.write(subject + "," + str(time) + "\n")


study = load_study()

print("現在の勉強記録")

for subject, time in study.items():

    print(subject, ":", time, "時間")


subject = input("追加する教科:")

time = int(input("勉強時間:"))

study[subject] = time

save_study(study)

print("保存しました！")