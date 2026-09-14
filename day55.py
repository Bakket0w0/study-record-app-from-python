study = {}
subject = input("教科:")
try:
    time = int(input("勉強時間:"))
    study[subject] = time
    print("追加しました")
except:
    print("数学を入力してください")
print(study)