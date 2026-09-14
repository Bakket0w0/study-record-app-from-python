subjects = ["数学", "英語", "国語"]

total = 0

for subject in subjects:
    time = int(input(subject + "の勉強時間："))
    total += time

print("合計勉強時間",total, "時間")

if total >= 5:
    print("よく頑張った！")
    


