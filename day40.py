study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

total = sum(study.values())
count = len(study)

average = total / count

print("合計", total,"時間")
print("教科数",count)
print("平均", average ,"時間")