subjects = ["数学","英語","国語"]
print("現在の教科")
for subject in subjects:
    print(subject)

print("教科数:",len(subjects))

new_subject = input("追加する教科:")

subjects.append(new_subject)
print("\n追加後")

for subject in subjects:
    print(subject)

print("教科数:",len(subjects))