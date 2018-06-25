# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from folhasp import items


class UltimasNoticiasSpider(scrapy.Spider):
    name = 'ultimas_noticias'
    #allowed_domains = ['folha.uol.com.br/']
    start_urls = ['https://m.folha.uol.com.br/ultimasnoticias/index.shtml']

    def parse(self, response):
        self.log("I'm visiting: " + response.url)
        sel = Selector(response)
        for li in sel.xpath("//ul[@class='list-fol']//li[position()>1]"):
            self.log(
                'titulo: ' + li.xpath("./a/text()").extract_first() + ',\n' +
                'categoria: ' + li.xpath("./section/a/text()").extract_first() + ',\n' +
                'hora: ' + li.xpath("./time/text()").extract_first()
            )
            yield {
                'titulo': li.xpath("./a/text()").extract_first(),
                'categoria': li.xpath("./section/a/text()").extract_first(),
                'hora': li.xpath("./time/text()").extract_first(),
                'link': li.xpath("./a/@href").extract_first()
            }