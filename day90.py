class studyrecord:
    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":",self.time, "時間")

    def add_time(self, time):
        self.time += time

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

class studymaneger:
    def __init__(self):
        self.records = []

    def add_record(self,record):
        self.records.append(record)

    def show_all(self):
        for record in self.records:
            record.show()

    def get_total(self):
        total = 0
        for record in self.records:
            total += record.get_time()
        return total

    def get_average(self):
        if len(self.records) == 0:
            return 0

        return self.get_total() / len(self.records)

    def get_best(self):
        if len(self.records) == 0:
            return None

        best = self.records[0]
        for record in self.records:
            if record.get_time() > best.get_time():
                best = record

        return best

manager =  studymaneger()

math = studyrecord("数学", 50)
english = studyrecord("英語", 30)
japanese = studyrecord("国語", 20)
science = studyrecord("理科", 10)
history = studyrecord("歴史", 40)

manager.add_record(math)
manager.add_record(english)
manager.add_record(japanese)
manager.add_record(science)
manager.add_record(history)

print("===　勉強記録　===")
manager.show_all()

print()

print("合計:", manager.get_total(), "時間")
print("平均:", manager.get_average(), "時間")

print()

print("一番勉強した科目:")
manager.get_best().show()