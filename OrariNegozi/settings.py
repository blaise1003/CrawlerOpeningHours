# Scrapy settings for OrariNegozi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'OrariNegozi'

SPIDER_MODULES = ['OrariNegozi.spiders']
NEWSPIDER_MODULE = 'OrariNegozi.spiders'

# Set delay between requests to go over google block
DOWNLOAD_DELAY = 5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'OrariNegozi (+http://www.yourdomain.com)'
