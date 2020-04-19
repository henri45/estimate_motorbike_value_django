from django.shortcuts import render
#from scraper_django_v1.scrapy_project_v1.spiders.spider_motorbike import MotorbikeWesterncapeSpider
import os
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from crochet import setup
from importlib import import_module
from scrapy.utils.log import configure_logging

# Create your views here.
setup()

def crawl(request):
  os.chdir("scraper_django_v1/scrapy_project_v1")
  module_name="scraper_django_v1.scrapy_project_v1.spiders.{}".format('spider_motorbike')
  scrapy_var = import_module(module_name)   #do some dynamic import of selected spider
  spiderObj=scrapy_var.MotorbikeWesterncapeSpider           #get mySpider-object from spider module

  # 'followall' is the name of one of the spiders of the project.
  configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
  crawler = CrawlerRunner(get_project_settings())
  crawler.crawl(spiderObj)
  os.chdir("../..")
  print("view ok")
  return render(request, "hello.html")
