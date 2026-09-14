study = {
    "数学":3,
    "英語":2
}
while True:
    print("1:記録を見る")
    print("2:記録を追加")
    print("3:終了")

    choice = input("選んでください")

    if choice =="1":
        print("勉強記録")
        print(study)

    elif choice =="2":
        subject = input("科目:")
        time = int(input("時間:"))
        study[subject] = time 
        print("追加しました！")
    
    elif choice =="3":
        print("終了します")
        break