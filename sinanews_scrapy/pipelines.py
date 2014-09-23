# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import sinanews_scrapy.settings as settings

import sqlite3
from datetime import datetime

class SinanewsScrapyPipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect(settings.OUTPUT_FILE)
        self.cursor = self.conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS news_data (
title, source, public_time, text, crawltime);
CREATE INDEX IF NOT EXISTS title_idx on news_data(title);
CREATE INDEX IF NOT EXISTS crawltime_idx on news_data(crawltime);'''
        self.cursor.executescript(sql)

    def process_item(self, item, spider):
        sql = u'''INSERT INTO news_data 
(title, source, public_time, text, crawltime)
values ('{title}', '{source}', '{public_time}', '{text}', '{crawltime}')'''
        sql = sql.format(title = item['title'].replace("'", "''"),
                source = item['source'].replace("'","''"),
                public_time = item['public_time'],
                text = item['text'].replace("'","''"),
                crawltime = str(datetime.now()))
        self.cursor.execute(sql)
        self.conn.commit()
        return item
    
    def spider_closed(self, spider):
        self.conn.close()

