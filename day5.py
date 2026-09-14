study = {
    "数学":5,
    "英語":3,
    "国語":2
}

best_subject =""
best_time = 0

for subject in study:
    if study[subject] > best_time:
        best_time = study[subject]
        best_subject = subject

print("一番勉強した科目", best_subject)
print("勉強時間",best_time)