# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import sinanews_scrapy.settings as settings
from sinanews_scrapy.NewsDataDB import NewsDataDB

from datetime import datetime

class SinanewsScrapyPipeline(object):

    def __init__(self):
        self.db = NewsDataDB(user = settings.DATABASE['user'],
                             password = settings.DATABASE['password'],
                             dbms = settings.DATABASE['dbms'])
        
    def process_item(self, item, spider):
        data_item = self.db.NewsData()
        
        data_item.title = item['title']
        data_item.source = item['source']
        data_item.public_time = item['public_time']
        data_item.body = item['body']

        self.db.add(data_item)
        self.db.commit()
       
        return item
    
    def spider_closed(self, spider):
        self.db.close()

