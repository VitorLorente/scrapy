# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item


class ultimasNoticias(scrapy.Item):
    titulo = scrapy.Field()
    categoria = scrapy.Field()
    hora = scrapy.Field()
    link = scrapy.Field()
