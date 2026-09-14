study = {}
total = 0

while True:
    subject = input("科目名(終了で終わる):")

    if subject == "終了":
        break
    time = int(input("勉強時間："))

    study[subject] = time
    total += time

print("勉強記録")
print(study)
print("合計勉強時間：", total,"時間")

best_subject = ""

best_time = 0

for subject in study:

    if study[subject] > best_time:

        best_time = study[subject]

        best_subject = subject

print("一番勉強した科目:", best_subject)

print("勉強時間:", best_time)