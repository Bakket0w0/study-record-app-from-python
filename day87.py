class studyrecord:
    def __init__(self, subject, time):
        self.subject = subject
        self.time = time 

    def show(self):
        print(self.subject, ":", self.time,"時間")

    def add_time(self, time):
        self.time = time 

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

math = studyrecord("数学", 50)
english = studyrecord("英語", 20)
japanese = studyrecord("国語", 15)
science = studyrecord("理科", 25)

records = [math, english, japanese, science]

best_record = records[0]

for record in records:
    if record.get_time() > best_record.get_time():
        best_record = record

print("一番勉強した科目は")
best_record.show()
