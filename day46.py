study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

file = open("study.txt","w", encoding="utf-8")
for subject, time in study.items():
    file.write(subject + ","+str(time)+ "\n")
file.close()
print("保存しました！")