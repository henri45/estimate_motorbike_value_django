# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import boto3
#from final_local.models import Ads_motorbike, db_connect, create_table

class GumtreeScraperPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com")

    def process_item(self, item, spider):
        """Save ads in the database
        This method is called for every item pipeline component
        """
        print('SUPER')
        table = self.dynamodb.Table('ads')
        table.put_item(
           Item=dict(item)
        )
        print("ok")
        return item
