# -*- coding: utf-8 -*-
import scrapy
from scraper_django_v1.scrapy_project_v1.items import ScrapyProjectV1Item
from scrapy.loader import ItemLoader
import datetime
from .utilis import convert_price, convert_date, convert_views


class MotorbikeWesterncapeSpider(scrapy.Spider):
    name = 'motorbike_westerncape'
    #allowed_domains = ['https://www.gumtree.co.za/s-motorcycles-scooters/western-cape/v1c9027l3100001p1']
    start_urls = ['https://www.gumtree.co.za/s-motorcycles-scooters/v1c9027p1']


    def parse(self, response):
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
      item = ScrapyProjectV1Item()
      item['url'] = response.request.url
      item['title'] = response.xpath("//h1/text()").extract_first()
      item['price'] = convert_price(response.xpath("//h3/descendant::text()").extract_first())
      item['creation_date'] = convert_date(response.xpath("//div[@class = 'vip-stats']//span[@class = 'creation-date']/text()").extract_first())
      item['views'] = convert_views(response.xpath("//div[@class = 'vip-stats']//span[@class = 'view-count']//span/text()").extract_first())
      item['location'] = response.xpath("//div[@class = 'vip-general-details']//div[@class = 'location']//a//text()").extract_first()
      item['description'] = "".join(response.xpath("//div[@class = 'description-content']/descendant::text()").extract())
      item['date_scraping'] = datetime.datetime.now()

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
        item[name] = attribute.css(".value::text").get()


      return item



