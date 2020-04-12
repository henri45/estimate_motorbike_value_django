from django.core.management.base import BaseCommand
from scraper_django_v1.scrapy_project_v1.spiders.spider_motorbike import MotorbikeWesterncapeSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
  help = "Release the spiders"

  def handle(self, *args, **options):
      process = CrawlerProcess(get_project_settings())

      process.crawl(MotorbikeWesterncapeSpider)
      process.start()
