# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class OrarinegoziItem(Item):
    # define the fields for your item here
    url = Field()
    name = Field()
    address = Field()
    openings = Field()
