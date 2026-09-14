class StudyRecord:

    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":", self.time, "時間")

    def get_time(self):
        return self.time


class StudyManager:

    def __init__(self):
        self.records = []

    def add_subject(self, subject, time):
        record = StudyRecord(subject, time)
        self.records.append(record)

    def show_all(self):
        for record in self.records:
            record.show()


manager = StudyManager()

print("=== 勉強記録アプリ ===")

subject = input("教科を入力してください: ")
time = int(input("勉強時間を入力してください: "))

manager.add_subject(subject, time)

print()
print("=== 登録された記録 ===")

manager.show_all()

manager.add_subject(subject, time)

print()
print("=== 現在の勉強記録 ===")
manager.show_all()