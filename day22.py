study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}

def show_study():
    print("勉強記録")
    for subject,time in study.items():
        print(subject,":", time,"時間")

show_study()