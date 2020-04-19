# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import re
import datetime

def convert_price(text):
  if "Contact for Price" in text or "Negotiable" in text:
    return -1
  price = ''.join(filter(str.isdigit, text))
  return int(price)

def convert_date(text):
  if "minute" in text:
    return str(datetime.date.today())

  if "an hour ago" in text:
    return str(datetime.date.today())

  if "a day ago" in text:
    return str(datetime.date.today() - datetime.timedelta(days=1))

  if "days" in text:
    days = int(''.join(filter(str.isdigit, text)))
    return str(datetime.date.today() - datetime.timedelta(days=days))

  if "a month ago" in text:
    return str(datetime.date.today() - datetime.timedelta(days=30))

  if "hours" in text:
    hours = int(''.join(filter(str.isdigit, text)))
    if datetime.datetime.now().hour > hours:
      return str(datetime.date.today())
    else:
      return str(datetime.date.today() - datetime.timedelta(days=1))

  if "months" in text:
    months = int(''.join(filter(str.isdigit, text)))
    return str(datetime.date.today() - datetime.timedelta(days=30*months))


def convert_views(text):
  views = int(''.join(filter(str.isdigit, text)))
  return views

class AdsItem(scrapy.Item):

    url = scrapy.Field(
      output_processor=TakeFirst()
    )

    title = scrapy.Field(
      output_processor=TakeFirst()
    )

    price = scrapy.Field(
      input_processor=MapCompose(convert_price),
      output_processor=TakeFirst()
    )

    creation_date = scrapy.Field(
      input_processor=MapCompose(convert_date),
      output_processor=TakeFirst()
    )

    views = scrapy.Field(
      input_processor=MapCompose(convert_views),
      output_processor=TakeFirst()
    )

    location = scrapy.Field(
      output_processor=TakeFirst()
    )

    description = scrapy.Field(
      output_processor=Join()
    )

    seller_type = scrapy.Field(
      output_processor=TakeFirst()

    )

    make = scrapy.Field(
      output_processor=TakeFirst()
    )

    model = scrapy.Field(
      output_processor=TakeFirst()
    )

    engine_displacement = scrapy.Field(
      output_processor=TakeFirst()
    )

    year = scrapy.Field(
      output_processor=TakeFirst()
    )

    kilometers = scrapy.Field(
      output_processor=TakeFirst()
    )

    date_scraping = scrapy.Field(
      output_processor=TakeFirst()
    )



