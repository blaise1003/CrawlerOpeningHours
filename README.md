CrawlerOpeningTimes
===================


1.0
===

This is an effective appliucation of Scrapy tool (scrapy.org).
CrawlerOpeningHours application crawl google serch results for site www.xxxxx.it.
For any result, CrawlerOpeningTimes parses response html in order to acquire informations about shops of italian GDO like 'name', 'addresses', 'opening times'.


Requirements
============

1. Python 2.7
2. Scrapy 0.16.4


Installation
============

1. Create a virtualenv with python2.7:  
    $ mkdir Scrapy  
    $ cd Scrapy  
    $ python2.7 ../virtualenv.py --distribute --no-site-packages .  
2. Activate virtualenv:  
    $ source bin/activate  
3. Install scrapy:  
    $ easy_install scrapy  
4. Clone GIT repository from GitHub:  
    $ git clone git@github.com:blaise1003/CrawlerOpeningHours.git CrawlerOpeningTimes



Start application
=================

To start CrawlerOpeningTimes application run command from application directory:  
    $ scrapy crawl shops -o shops.json -t json

Previous command starts crawl and write an oputput file in json format (path-to-venv-directory/CrawlerOpeningTimes/shops.json) with shops informations.
