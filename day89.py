class studyrecord:
    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":",self.time, "時間")

    def add_tie(self, time):
        self.time += time 

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

math = studyrecord("数学", 40)
english = studyrecord("英語", 30)
japanese = studyrecord("国語", 20)
science = studyrecord("理科", 10)

records = [math, english, japanese,science]

total_time = 0

for record in records:
    total_time += record.get_time()

average_time = total_time / len(records)

print("全科目の勉強時間は", total_time, "時間です")
print("平均勉強時間は", average_time, "時間です")