study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

print("今日の勉強記録")
for subject, time in study.items():
    print(subject,":", time,"時間")

delete_subject = input("削除する教科:")

if delete_subject in study:
    del study[delete_subject]
    print("削除しました")

else:
    print("その教科はありません")
print("\n現在の勉強記録")
for subject, time in study.items():
    print(subject, ":", time, "時間")