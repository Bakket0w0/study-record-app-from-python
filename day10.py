file = open("study.txt","r")

data = file.read()

file.close()

print("前回の記録")
print(data)