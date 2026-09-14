study ={
    "数学":10,
    "英語":20,
    "国語":4,
    "情報":15
}

subject = input("削除する科目名:")
if subject in study:
    del study[subject]
    print(subject+"を削除しました")
else:
    print("その科目はありません")

print("現在のデータ:")
print(study)