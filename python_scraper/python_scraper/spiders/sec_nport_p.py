# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class SecNPORTPSpider(scrapy.Spider):
    name = 'sec_nport_p'
    allowed_domains = ['sec.report']
    start_url = 'https://sec.report/Document/Header/?formType=NPORT-P&keyword=corporate'
    start_pages = 8

    def start_requests(self):
        for page in range(1, self.start_pages+1):
            yield Request(f'{self.start_url}&page={page}', callback=self.parse)

    def parse(self, response):
        for url in response.xpath('//table//tr/td[2]/a/@href').extract():
            yield response.follow(f'{url}primary_doc.xml', callback=self.parse_xml)

    def parse_xml(self, response):
        print(response)
