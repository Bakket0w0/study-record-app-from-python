study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
def show_total():
    total = sum(study.values())
    print("合計",total)

def show_average():
    total = sum(study.values())
    average = total/ len(study)
    print("平均", average)

show_total()
show_average()