from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime

sched = BlockingScheduler()

#在每天7-22點,每20分鐘執行一次
@sched.scheduled_job("cron",hour="7-22",minute="*/20")
def scheduled_job():
    print("=======APS喚醒程式執行中=======")
    print(f"{datetime.datetime.now().ctime()}")
    print("=======APS喚醒程式執行中=======")

    url = "https://ryder1.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key,value in conn.getheaders():
        print(key,value)


sched.start()