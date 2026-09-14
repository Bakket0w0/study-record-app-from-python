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


def save_study(study):

    with open("study.txt", "w", encoding="utf-8") as file:

        for subject, time in study.items():

            file.write(subject + "," + str(time) + "\n")


study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}


update_subject(study)

save_study(study)

print("保存しました！")