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

    def show_all(self):
        for record in self.records:
            record.show()


manager = StudyManager()

print("=== 勉強記録アプリ ===")

while True:
    subject = input("教科を入力してください（終了するなら q）: ")

    if subject == "q":
        break

    time = int(input("勉強時間を入力してください: "))

    manager.add_subject(subject, time)

    print()
    print("=== 現在の勉強記録 ===")
    manager.show_all()
    print()

print("=== 最終的な勉強記録 ===")
manager.show_all()