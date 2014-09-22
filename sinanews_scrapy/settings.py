# Scrapy settings for sinanews_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'sinanews_scrapy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['sinanews_scrapy.spiders']
NEWSPIDER_MODULE = 'sinanews_scrapy.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOAD_TIMEOU = 30
LOG_LEVEL = 'INFO'
LOG_FILE='sinanews_scrapy.log'
