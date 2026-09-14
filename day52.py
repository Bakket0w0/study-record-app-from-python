study = {}
file = open("study.txt","r",encoding="utf-8")
for line in file:
    subject, time = line.strip().split(",")
    study[subject]= int(time)
file.close()
print("現在の勉強記録")
for subject, time in study.items():
    print(subject,":",time,"時間")

subject = input("追加する教科")
time = int(input("勉強時間:"))
study[subject] = time
file = open("study.txt","w",encoding="utf-8")

for subject, time  in study.items():
    file.write(subject + "," + str(time)+ "\n")

file.close()
print("保存しました！")