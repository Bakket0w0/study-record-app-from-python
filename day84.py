class studyrecord:
    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":",self.time, "時間")

    def add_time(self,time):
        self.time += time

    def change_time(self, time):
        self.time = time

math = studyrecord("数学", 30)
math.show()
math.change_time(60)
math.show()

english = studyrecord("英語", 20)
english.show()
english.change_time(45)
english.show()