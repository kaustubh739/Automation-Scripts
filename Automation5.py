import schedule
import time
import datetime


def MySchedule():
    print("Inside MySchedule function at : ",datetime.datetime.now())

def MyScheduleX():
    print("Inside MyScheduleX function at : ",datetime.datetime.now())

def main():
    print("Inside automation script")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    schedule.every(1).minute.do(MyScheduleX)

    #schedule.every(1).hour.do(MyScheduleX)

    print("Application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
# consider below phthon application which schedule task after minute, hour as well as on specific day or specific time.

'''import time
import schedule
import datetime

def fun_Minute():
    print("current time is ")
    print(datetime.datetime.now())
    print("schedular executed after minute")

def fun_Hour():
    print("curent time is")
    print(datetime.datetime.now())
    print("schedular executed after hour")
    
def fun_Day():
    print("current time is")
    print(datetime.datetime.now())
    print("schedular executed after day")

def fun_Afternoon():
    print("current time is")
    print(datetime.datetime.now())
    print("schedular executed at 12")

def main():
    print("Python Automation & Machine Learning")

    print("python job schedular")
    print(datetime.datetime.now())

    schedule.every(1).minute.do(fun_Minute)

    schedule.every(1).hour.do(fun_Hour)

    schedule.every().day.at("00:00").do(fun_Afternoon)

    schedule.every().sunday.do(fun_Day)

    schedule.every().saturday.at("18:30").do(fun_Day)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()'''