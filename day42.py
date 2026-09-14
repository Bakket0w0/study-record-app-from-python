study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
subject = min(study, key=study.get)
print("一番少ない教科")
print(subject)
print(study[subject],"時間")