study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
subject = max(study, key=study.get)

print("一番勉強した教科")
print(subject)
print(study[subject],"時間")