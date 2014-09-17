#  -*- coding=utf8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import json
import os.path

from sinanews_scrapy.items import SinanewsScrapyItem



class SinanewsSpider(CrawlSpider):
    name = 'sinanews'
    allowed_domains=['sina.com.cn']
    start_urls = ['http://search.sina.com.cn/?q=%CF%B0%BD%FC%C6%BD+%BD%B2%BB%B0&range=title&c=news&sort=time']

    """ 由于新浪的页面采用GB2312编码，所以在处理下一页时候的xpath语句要进行编
    码转换所以此处不再直接用XPath找GBK编码的“下一页”，而是找它的上一级那个框"""

    rules = [Rule(LinkExtractor(allow = '/.+/\d+.shtml',
        deny = '/171826152112.shtml'),
        'parse_news'),
        Rule(LinkExtractor(restrict_xpaths = "//div[@class='pagebox']"), 
            'parse_next_page')]

    def parse_news(self, response):
        news = SinanewsScrapyItem()
        temp_dict = {}

        temp_dict['title'] = \
                response.xpath("//h1[@id='artibodyTitle']//text()").extract()[0]

        temp_dict['source'] = \
                response.xpath("//span[@id='media_name']//text()").extract()[0]

        temp_dict['public_time'] = \
                response.xpath("//span[@id='pub_date']//text()").extract()[0]

        temp = response.xpath("//div[@id='artibody']//p//text()").extract()
        temp_dict['text'] = '\n'.join(temp)

        with open(os.path.join('temp',temp_dict['title']), 'w') as f:
            json.dump(temp_dict, f)
        
        news['title'] = temp_dict['title']
        news['source'] = temp_dict['source']
        news['public_time'] = temp_dict['public_time']
        news['text'] = temp_dict['text']

        return news
    
    def parse_next_page(self, response):
        print('--------------------------------------------------------------')
        print(response.url)
        self.make_requests_from_url(response.url)


