# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector

from OrariNegozi.items import OrarinegoziItem


class OrarinegoziSpider(CrawlSpider):
    """
    custom spider for grab shops information from www.doveconviene.it
    """
    name = 'shops'
    allowed_domains = ['doveconviene.it', 'google.it']
    start_urls = [
        'https://www.google.it/search?q=site:www.doveconviene.it/negozi/']
    rules = [
        # shop url on www.doveconviene.it website
        Rule(
            SgmlLinkExtractor(
                allow=[r'\b/negozi/\b'],
                deny=[r'\bwebcache\b'],
                restrict_xpaths=('//div[@id="ires"]')
            ),
            callback='parse_shops',
            follow=False
        ),
        # next results page url
        Rule(
            SgmlLinkExtractor(
                allow=[r'\b&start=\b'],
                restrict_xpaths=('//div[@id="navcnt"]')
            ),
            follow=True
        ),
    ]
    weekdays = [
        (1, u"Lunedì"),
        (2, u"Martedì"),
        (3, u"Mercoledì"),
        (4, u"Giovedì"),
        (5, u"Venerdì"),
        (6, u"Sabato"),
        (7, u"Domenica")
    ]

    def normalize_address(self, address_list=[]):
        """
        minor fix on address string format
        """
        address = []
        for item in address_list:
            item = item.replace(u'\t', '').replace(u'\n', '')
            if item:
                address.append(item.decode('utf-8'))
        return item

    def parse_shops(self, response):
        x = HtmlXPathSelector(response)

        item = OrarinegoziItem()
        item['url'] = response.url
        item['name'] = x.select(
            "//div[@class='filiale-box-content']/h2/b/a/text()"
        ).extract()[0].decode('utf-8')
        item['address'] = self.normalize_address(
            x.select(
                "//div[@class='filiale-box-content']/h2/text()"
            ).extract()
        )
        openings = []
        for wdi, wdn in self.weekdays:
            wd_opening = x.select(
                "//div[@class='filiale-box-contatti']" + \
                "/table/tr[2]/td[%s]/span/text()" % \
                str(wdi)
            ).extract()
            openings.append(
               {'wd_name': wdn, 'wd_opening': wd_opening}
            )
        item['openings'] = openings
        return item


spider = OrarinegoziSpider()
