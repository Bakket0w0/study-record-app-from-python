class studyrecord:
    def __init__(self, subject ,time):
        self.time = time
        self.subject = subject

    def show(self):
        print(self.subject, ":",self.time, "時間")

    def add_time(self, time):
        self.time += time 

    def change_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

math = studyrecord("数学", 50)
english = studyrecord("英語", 40)
japanese = studyrecord("国語", 5) 
science  = studyrecord("理科",75) 

records = [math, english, japanese, science]

total_time = 0

for record in records:
    total_time += record.get_time()

print("全科目の勉強時間は",total_time, "時間です")