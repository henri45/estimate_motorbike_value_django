from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scraper_django_v1.scrapy_project_v1.runspider import runspider

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(runspider, 'interval', minutes=5)
    scheduler.start()
