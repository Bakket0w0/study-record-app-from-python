class StudyRecord:

    def __init__(self, subject, time):
        self.subject = subject
        self.time = time

    def show(self):
        print(self.subject, ":",self.time,"時間")

math = StudyRecord("数学", 30)
english = StudyRecord("英語", 20)

math.show()
english.show()