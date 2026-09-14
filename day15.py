study = {
    "数学":10,
    "英語":20,
    "国語":4,
    "情報":15
}

best_subject = ""
best_time = 0

for subject in study:
    if study[subject]>best_time:
        best_time = study[subject]
        best_subject = subject
print("一番勉強した科目",best_subject)
print("勉強時間", best_time)        