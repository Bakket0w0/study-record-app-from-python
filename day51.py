study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
subject = input("追加する教科:")
time = int(input("勉強記録:"))

study[subject] = time

file = open("study.txt", "w", encoding="utf-8")
for subject, time in study.items():
    file.write(subject+","+str(time)+"\n")

file.close()
print("保存しました！")