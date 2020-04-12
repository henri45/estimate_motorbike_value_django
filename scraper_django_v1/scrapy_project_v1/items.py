# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from scraper_django_app.models import Ads_motorbike

class ScrapyProjectV1Item(DjangoItem):
  django_model = Ads_motorbike
