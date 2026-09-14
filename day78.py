def delete_subject(study):

    subject = input("削除する教科:")

    if subject in study:

        del study[subject]

        print("削除しました！")

    else:

        print("その教科はありません")


study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}


delete_subject(study)

print("\n削除後")

for subject, time in study.items():

    print(subject, ":", time, "時間")