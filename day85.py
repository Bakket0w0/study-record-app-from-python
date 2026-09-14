class studyrecord:
    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":", self.time, "時間")

    def add_time(self, time):
        self.time += time

    def change_time (self,time):
        self.time = time

    def get_time(self):
        return self.time

math = studyrecord("数学", 30)
math.show()
time = math.get_time()
print("数学の勉強時間は", time, "時間です")

english = studyrecord("英語", 20)
english.add_time(15)
time = english.get_time()
print("英語の勉強時間は", time , "時間です")