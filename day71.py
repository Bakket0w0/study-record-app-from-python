def get_total(study):
    return sum(study.values())
def get_average(study):
    if len(study)== 0:
        return 0
    return sum (study.values())/ len (study)

study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

total = get_total(study)
average = get_average(study)

print("合計:", total,"時間")
print("平均:", average, "時間")