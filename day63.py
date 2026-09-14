def get_total(study):
    total = sum(study.values())
    return total
study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
total = get_total(study)
print("合計:", total,"時間")