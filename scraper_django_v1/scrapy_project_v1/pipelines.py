# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyProjectV1Pipeline(object):
    def process_item(self, item, spider):
      dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com")
      try:
        table = dynamodb.Table('ads')
      except
        print("Table doesn't exist")

      response = table.put_item(
         Item={
              'url' : item.url
              'title': item.title
              'price': item.price
              'creation_date': item.creation_date
              'views': item.views
              'location': item.location
              'description': item.description
              'seller_type': item.seller_type
              'make': item.make
              'model': item.model
              'engine_displacement': item.engine_displacement
              'year': item.year
              'kilometers': item.kilometers
              'date_scraping': item.date_scraping
          }
      )

      print(item.title, " in the DB")
