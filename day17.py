study = {
    "数学": 10,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

subject = input("科目名:")

if subject in study:
    print(subject + "の勉強時間は")
    print(study[subject], "時間です")
else:
    print("その科目はありません")