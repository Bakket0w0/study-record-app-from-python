def save_study(study):
    with open("study.txt","w",encoding="utf-8")as file:
        for subject, time in study.items():
            file.write(subject + "," + str(time) + "\n")
    print("保存しました！")
study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

save_study(study)