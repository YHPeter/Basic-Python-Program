def tips ():
    import datetime
    mot=["今天星期一",
         "今天星期二",
         "今天星期三",
         "今天星期四",
         "今天星期五",
         "今天星期六",
         "今天星期日"]
    day = datetime.datetime.now().weekday()
    print(mot[day])
tips()
