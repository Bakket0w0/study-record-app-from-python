study = {
    "数学":30,
    "英語":20,
    "国語":4,
    "情報":15
}

def get_time(subject):
    return study[subject]
print(get_time("数学"))
print(get_time("情報"))
print(get_time("英語"))