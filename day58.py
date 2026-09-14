import random
study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

subject = random.choice(list(study.keys()))
print("今日おすすめの強化")
print(subject)
print("現在の勉強時間")
print(study[subject], "時間")
