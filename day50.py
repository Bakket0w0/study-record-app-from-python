study = {}
file= open("study.txt","r",encoding="utf-8")
for line in file:
    subject, time = line.strip().split(",")
    study[subject] = int(time)
file.close()
print("現在の勉強記録")
for subject, time in study.items():
    print(subject,":",time,"時間")