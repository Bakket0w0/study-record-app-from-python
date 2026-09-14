study = {
    "数学": 30,
    "英語": 20,
    "国後": 4,
    "情報": 15
}

def show_ranking():
    ranking = sorted(
        study.items(),
        key=lambda item: item[1],
        reverse= True
    )
    print("\n=== 勉強時間ランキング ===")
    for number, (subject, time) in enumerate(ranking, start=1):
        print(number, "位:", subject, time, "時間")
show_ranking()
