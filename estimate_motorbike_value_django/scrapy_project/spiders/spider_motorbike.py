# -*- coding: utf-8 -*-
import scrapy
from estimate_motorbike_value_django.scrapy_project.items import AdsItem
from scrapy.loader import ItemLoader
import datetime


count_item = 0
class MotorbikeWesterncapeSpider(scrapy.Spider):
    name = 'motorbike_westerncape'
    #allowed_domains = ['https://www.gumtree.co.za/s-motorcycles-scooters/western-cape/v1c9027l3100001p1']
    start_urls = ['https://www.gumtree.co.za/s-motorcycles-scooters/v1c9027p1']

    ads_item = ItemLoader()


    def parse(self, response):
      print("coucou")
      links_ads = response.xpath("//div[@class='title mult-lines-lt-1280']//@href").getall()

      ##Start with the start_urls
      for link in links_ads:
        ##go and parse all the ads

        ads = response.urljoin(link)
        #count_item += 1
        yield scrapy.Request(ads, callback = self.parse_ads)
        #yield scrapy.Request(ads, callback = self.parse_ads)

      #Go to the next page
      #next_page = response.xpath("//*[contains(@class,'icon-pagination-right')]//@href").get()
      #if next_page is not None:
      #  next_page_link = response.urljoin(next_page)
      #  yield scrapy.Request(next_page_link, callback = self.parse)

    #parse an ads.
    def parse_ads(self, response):
      print("parse_ads")
      loader = ItemLoader(item=AdsItem(), response = response)
      loader.add_value('url', response.request.url)
      loader.add_xpath('title', "//h1/text()")
      loader.add_xpath('price', "//h3/descendant::text()")
      loader.add_xpath('creation_date', "//div[@class = 'vip-stats']//span[@class = 'creation-date']/text()")
      loader.add_xpath('views', "//div[@class = 'vip-stats']//span[@class = 'view-count']//span/text()")
      loader.add_xpath('location', "//div[@class = 'vip-general-details']//div[@class = 'location']//a//text()")
      loader.add_xpath('description', "//div[@class = 'description-container']/descendant::text()")
      loader.add_value('date_scraping', str(datetime.datetime.now()))
      #ads_data['name_seller'] = response.xpath("//div[@class = 'reply-title']/descendant::text()").get()
      attributes = response.xpath("//div[@class = 'attributes']/*")


      #For each ads, there is a list of attributes.
      for attribute in attributes:
        name = attribute.css(".name::text").get()

        if "Location" in name:
          continue
        if "For Sale By:" in name:
          name = "seller_type"
        if "Make:" in name:
          name = "make"
        if "Year" in name:
          name = "year"
        if "Model" in name:
          name = "model"
        if "Kilometers:" in name:
          name = "kilometers"
        if "Engine Displacement" in name:
          name = "engine_displacement"
        loader.add_value(name, attribute.css(".value::text").get())

      ads_item = loader.load_item()
      print(ads_item)

      return ads_item
