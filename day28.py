def show_menu():
    print("1:勉強記録を見る")
    print("2:終了")

show_menu()

choice = input("番号を入力:")

if choice == "1":
    print("勉強記録です")

elif choice == "2":
    print("終了します")

else:
    print("その番号はありません")