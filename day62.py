def show_total(study):
    total = sum(study.values())
    print("合計:", total,"時間")

study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
show_total(study)