study = {
    "数学": 10,
    "英語": 2,
    "国語": 4,
    "情報": 5
}

total = 0

for subject in study:
    total+=study[subject]

average = total/len(study)

print("合計勉強時間",total)
print("合計勉強時間",average)