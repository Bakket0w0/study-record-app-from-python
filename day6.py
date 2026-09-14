study = {}
total = 0

for i in range(2):
 subject = input("科目名：")
 time = int(input("勉強時間："))

 study[subject] = time
 total += time
print("勉強記録")
print(study)

print("合計勉強時間：",total,"時間")