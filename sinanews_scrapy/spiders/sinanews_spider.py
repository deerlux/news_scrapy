#  -*- coding=utf8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log

import json
import os.path

from sinanews_scrapy.items import SinanewsScrapyItem

class SinanewsSpider(CrawlSpider):
    name = 'sinanews'
    allowed_domains=['sina.com.cn']
    start_urls = ['http://search.sina.com.cn/?q=%CF%B0%BD%FC%C6%BD+%BD%B2%BB%B0&range=title&c=news&sort=time']

    '''follow=True 很关键啊，也很漂亮了，只想自己再写一个回调函数如何跟踪这个
链接呢，原来有更方便的实现方法，害我白熬了两个小时的夜，github上找实例很重要
啊，感谢geekan大侠的例子啊。'''

    rules = [Rule(LinkExtractor(allow = '/.+/\d+.shtml',
        deny = '/171826152112.shtml'),
        'parse_news'),
        Rule(LinkExtractor(restrict_xpaths = u"//a[@title='下一页']"), 
            callback = 'parse_next')]

    def parse_news(self, response):
        news = SinanewsScrapyItem()

        temp = response.xpath("//h1[@id='artibodyTitle']//text()").extract()
        news['title'] = temp[0] if temp else ''

        temp = response.xpath("//span[@id='media_name']//text()").extract()
        news['source'] = temp[0] if temp else ''
        
        
        temp =  response.xpath("//span[@id='pub_date']//text()").extract()
        news['public_time'] = temp[0] if temp else ''

        temp = response.xpath("//div[@id='artibody']//p//text()").extract()
        news['text'] = '\n'.join(temp) if temp else ''

        log.msg(': '.join([response.url, news['title']]), level=log.INFO)

        return news
    def parse_next(self, response):
        log.msg(response.url)
        return self.make_requests_from_url(response.url)
