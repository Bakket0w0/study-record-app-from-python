subjects = ["数学", "英語", "国語"]

study = {}

for subject in subjects:
    time = int(input(subject + "の勉強時間："))
    study[subject] = time

for subject in study:
    print(subject,study[subject],"時間")

