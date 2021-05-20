# -*- coding: utf-8 -*-
import sys
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger


scheduler = BackgroundScheduler()

def print_start_time(func):
    def wrapper(*args, **kwargs):
        sys.stdout.write(time.strftime("[%Y-%m-%d %H:%M:%S] "))
        return func(*args, **kwargs)
    return wrapper
    
    
@print_start_time
def test1(job_id):
    print("run test1")


@print_start_time
def test2():
    print("run test2")
    

@print_start_time
def test3():
    print("run test3")
    

@print_start_time
def test4():
    print("run test4")
    

@print_start_time
def test5():
    print("run test5")
    
    
scheduler.add_job(test1, trigger=DateTrigger(datetime.datetime.now() + datetime.timedelta(seconds=5)), args=("test_job_id",))
scheduler.add_job(test2, trigger=CronTrigger.from_crontab("* * * * *"))
scheduler.add_job(test3, trigger="cron", minute="*/2", hour="*", day="*", month="*", day_of_week="*")
scheduler.add_job(test4, trigger="interval", seconds=10)
scheduler.add_job(test5, trigger="interval", minutes=1)

scheduler.start()


while 1:
    time.sleep(1)
    # scheduler.print_jobs()
    