# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_djangoitem import DjangoItem

from company.models import Company
from python_scraper.items import CompanyItem


class PythonScraperPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DjangoItem):
            instance = item.instance
            commit = True
            if isinstance(item, CompanyItem) and Company.objects.filter(series_lei=instance.series_lei,
                                                                        rep_pd_date=instance.rep_pd_date).exists():
                # skip items already in database, define series_lei and rep_pd_date to be unique
                commit = False
            item.save(commit=commit)
        return item
