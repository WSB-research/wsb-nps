# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from python_scraper.items import CompanyItem


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
            yield response.follow(f'{url}primary_doc.xml', callback=self.parse_xml, headers={
                'Accept': 'application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en',
            })

    def parse_xml(self, response):
        response.selector.register_namespace('x', 'http://www.sec.gov/edgar/nport')
        yield CompanyItem(
            series_lei=response.xpath('//x:seriesLei/text()').extract()[0],
            name=response.xpath('//x:regName/text()').extract()[0],
            series_name=response.xpath('//x:seriesName/text()').extract()[0],
            rep_pd_date=response.xpath('//x:repPdDate/text()').extract()[0],
            total_assets=response.xpath('//x:totAssets/text()').extract()[0],
            total_liabilities=response.xpath('//x:totLiabs/text()').extract()[0],
            net_assets=response.xpath('//x:netAssets/text()').extract()[0],
        )
