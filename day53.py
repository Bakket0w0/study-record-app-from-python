study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

print("勉強時間ランキング")
for subject, time in sorted(study.items(),key=lambda item: item[1], reverse=True):
    print(subject,":", time,"時間")
