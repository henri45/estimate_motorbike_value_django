from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from crochet import setup
from importlib import import_module
from scrapy.utils.project import get_project_settings
import os
#from estimate_motorbike_value_django.scrapy_project.spiders.spider_motorbike import MotorbikeWesterncapeSpider

setup()

def runspider():
  os.chdir("estimate_motorbike_value_django/scrapy_project")
  module_name="estimate_motorbike_value_django.scrapy_project.spiders.{}".format('spider_motorbike')
  scrapy_var = import_module(module_name)   #do some dynamic import of selected spider
  spiderObj=scrapy_var.MotorbikeWesterncapeSpider           #get mySpider-object from spider module
  # 'followall' is the name of one of the spiders of the project.

  crawler = CrawlerRunner(get_project_settings())
  crawler.crawl(spiderObj)
  os.chdir("../..")
