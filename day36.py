subjects = ["数学", "英語", "国語"]

print("現在の教科")
for subject in subjects:
    print(subject)

new_subject = input("追加する教科:")

if new_subject in subjects:
    print("その教科はもう登録されています")

else:
    subjects.append(new_subject)
    print("追加しました")

print("\n現在の教科")

for subject in subjects:
    print(subject)