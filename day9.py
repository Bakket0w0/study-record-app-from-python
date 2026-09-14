subject = input("科目：")
time = input("時間：")

file = open("study.txt","w")

file.write(subject + "\n")
file.write(time)

file.close()
print("保存しました")