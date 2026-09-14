import random
study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

print("===今日の勉強アシスタント===")
subject = random.choice(list(study.keys()))
print("今日のおすすめ教科:", subject)
add = int(input("今日の勉強した時間:"))
study[subject] += add
print()
print("更新後")
for subject, time in study.items():
    print(subject,":", time,"時間")
print()
print("合計")
print(sum(study.values()), "時間")