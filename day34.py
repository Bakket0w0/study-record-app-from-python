study = {
    "数学": 30,
    "英語": 20,
    "国語": 4,
    "情報": 15
}
def show_menu():
    print("1:教科数を見る")
    print("2:終了")

def show_subject_count():
    print("登録されている教科数は",len(study),"個です")

show_menu()

choice = input("番号を入力:")

if choice =="1":
    show_subject_count()
elif choice == "2":
    print("終了します")

else:
    print("その番号はありません")