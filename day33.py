subjects = ["数学","英語","国語","情報"]

print("現在の教科")
for subject in subjects:
    print(subject)

delete_subject = input("削除する教科:")

if delete_subject in subjects:
    subjects.remove(delete_subject)
    print("\n削除しました")
else:
    print("\nその教科はありません")
print("\n現在の教科")

for subject in subjects:
    print(subject)