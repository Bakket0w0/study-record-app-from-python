study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15,
    "社会": 40


}

ranking = sorted(study.items(), key=lambda x:x[1], reverse=True)

for subject, time in ranking:
    print(subject,":", time, "時間")