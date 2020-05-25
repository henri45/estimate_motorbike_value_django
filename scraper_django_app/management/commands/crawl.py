from django.core.management.base import BaseCommand
from estimate_motorbike_value_django.scrapy_project.spiders.spider_motorbike import MotorbikeWesterncapeSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class Command(BaseCommand):
  help = "Release the spiders"

  def handle(self, *args, **options):
      os.chdir("estimate_motorbike_value_django/scrapy_project")
      process = CrawlerProcess(get_project_settings())

      process.crawl(MotorbikeWesterncapeSpider)
      process.start()
      os.chdir("../..")
