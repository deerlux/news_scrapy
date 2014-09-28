# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log

from datetime import datetime
import urllib

from xinhua_scrapy.items import XinhuaScrapyItem
import xinhua_scrapy.settings as settings


class XinhuaSpider(CrawlSpider):
    name = 'xinhua'
    allowed_domains = ['xinhuanet.com']

    search_url = 'http://info.search.news.cn/result.jspa?ss=2&t=1&t1=0&rp=10&btn=%CB%D1+%CB%F7&np=2&'
    keywords_code = (' '.join(settings.KEYWORDS)).encode('gbk')
    param = {'n1': keywords_code,'ct':keywords_code}
    search_url += urllib.urlencode(param)

    start_urls = [search_url]

#    start_urls = ['http://www.xinhuanet.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//span[@class="style1d"]'), 
            callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths = u'//a[contains(.//text(), "下一页")]'), 
        follow=True),
    )

    def parse_item(self, response):
        item = XinhuaScrapyItem()
        item['url'] = response.url
        item['crawl_time'] = datetime.now()
        item['domain'] = self.allowed_domains[0]
        item['keywords'] = ' '.join(settings.KEYWORDS)
        
        title_xpaths = ' | '.join(['//h1[@id="title"]//text()', 
            '//span[@id="title"]//text()',
            '//div[@class="title"]//text()',
            '//div[@class="title_tp"]'])
        temp = response.xpath(title_xpaths).extract()
        item['title'] = temp[0].strip() if temp else ''
       
        temp = response.xpath('//span[@id="pubtime"]//text()').extract()
        item['public_time'] = temp[0] if temp else ''

        temp = response.xpath('//font[@color="000066"]//text()').extract()
        item['source'] = temp[0] if temp else ''

        temp = response.xpath('//p//text()').extract()
        item['body'] = '\n'.join(temp) if temp else ''

        log.msg(item['title'], level=log.INFO)

        return item
