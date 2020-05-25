from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from estimate_motorbike_value_django.scrapy_project.runspider import runspider

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(runspider, 'interval', minutes=5)
    scheduler.start()
