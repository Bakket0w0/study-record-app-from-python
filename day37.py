study = {
    "数学": 30,
    "英語": 20,
    "国語": 4
}

print("現在の勉強記録")

for subject, time in study.items():
    print(subject, ":", time, "時間")

subject = input("追加する教科:")
time = int(input("勉強時間:"))

study[subject] = time

print("\n追加後")

for subject, time in study.items():
    print(subject, ":", time, "時間")