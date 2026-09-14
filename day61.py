study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
subject = input("教科:")
try:
    time =int(input("勉強時間:"))
    study[subject] = time
    print("追加しました！")
except ValueError:
    print("勉強時間には数字を入力してください")
print("\n現在の勉強記録")
for subject, time in study.items():
    print(subject,":", time, "時間")