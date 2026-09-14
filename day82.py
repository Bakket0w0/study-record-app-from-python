def add_subject(study):
    subject=input("教科:")
    time=int(input("勉強時間:"))

    study[subject]=time

    print("追加しました")


study={
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

print("=== 現在の勉強時間 ===")

for subject, time in study.items():
    print(subject,":", time,"時間")

print()

add_subject(study)

print("\n=== 追加後 ===")

for subject, time in study .items():
    print(subject, ":", time, "時間")