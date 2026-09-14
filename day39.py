study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

print("現在の勉強記録")

for subject, time in study.items():
    print(subject, ":", time, "時間")

update_subject = input("更新する教科：")

if update_subject in study:

    new_time = int(input("新しい勉強時間："))

    study[update_subject] = new_time

    print("更新しました")

else:
    print("その教科はありません")

print("\n更新後")

for subject, time in study.items():
    print(subject, ":", time, "時間")