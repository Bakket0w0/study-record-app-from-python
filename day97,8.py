class StudyRecord:

    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":", self.time, "時間")

    def add_time(self, time):
        self.time += time

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time


class StudyManager:

    def __init__(self):
        self.records = []

    def add_subject(self, subject, time):
        for record in self.records:
            if record.subject == subject:
                record.add_time(time)
                return

        record = StudyRecord(subject, time)
        self.records.append(record)

    def delete_subject(self, subject):
        for record in self.records:
            if record.subject == subject:
                self.records.remove(record)
                return True

        return False

    def change_time(self, subject, time):
        for record in self.records:
            if record.subject == subject:
                record.change_time(time)
                return True

        return False

    def show_all(self):
        if len(self.records) == 0:
            print("勉強記録がありません")
            return

        for record in self.records:
            record.show()

    def show_ranking(self):
        ranking = sorted(
            self.records,
            key=lambda record: record.get_time(),
            reverse=True
        )

        if len(ranking) == 0:
            print("勉強記録がありません")
            return

            print()
            print("=== 勉強時間ランキング ===")

            for i, record in enumerate(ranking, start=1):
                print(i, "位", record.subject, ":", record.get_time(), "時間")

    def show_statistics(self):

        if len(self.records) == 0:
            print("勉強記録がありません")
            return

        total = 0

        for record in self.records:
            total += record.get_time()

        average = total / len(self.records)

        best = self.records[0]

        for record in self.records:
            if record.get_time() > best.get_time():
                best = record

        print()
        print("=== 勉強統計 ===")
        print("合計勉強時間 :", total, "時間")
        print("平均勉強時間 :", average, "時間")
        print("一番勉強した教科 :", best.subject)


manager = StudyManager()


while True:

    print()
    print("=== 勉強記録アプリ ===")
    print("1. 教科を追加")
    print("2. 教科を削除")
    print("3. 勉強記録を表示")
    print("4. 勉強時間を変更")
    print("5. ランキング")
    print("6. 勉強統計")
    print("7. 終了")

    choice = input("選択してください: ")

    if choice == "1":

        subject = input("教科を入力してください: ")
        time = int(input("勉強時間を入力してください: "))

        manager.add_subject(subject, time)

        print()
        print("追加しました！")
        manager.show_all()

    elif choice == "2":

        subject = input("削除する教科を入力してください: ")

        if manager.delete_subject(subject):
            print(subject, "を削除しました")
        else:
            print(subject, "は登録されていません")

        print()
        manager.show_all()

    elif choice == "3":

        print()
        print("=== 現在の勉強記録 ===")
        manager.show_all()

    elif choice == "4":

        subject = input("変更する教科を入力してください: ")
        time = int(input("新しい勉強時間を入力してください: "))

        if manager.change_time(subject, time):
            print(subject, "の勉強時間を変更しました")
        else:
            print(subject, "は登録されていません")

        print()
        manager.show_all()

    elif choice == "5":

        manager.show_ranking()

    elif choice == "6":
        manager.show_statistics()

    elif choice == "7":
        print("アプリを終了します")
        break

    else:

        print("1〜7を入力してください")