study = {}
file = open("study.txt","r",encoding="utf-8")
for line in file:
    subject, time = line.strip().split(",")
    study[subject] = int(time)

file.close()
print(study)