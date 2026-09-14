study = {
    "数学": 5,
    "英語": 2,
    "国語": 4
}

total = 0

for subject in study:
    total += study[subject]

print("合計勉強時間:", total, "時間")