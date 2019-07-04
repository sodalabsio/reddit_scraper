# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class RedditPipeline(object):
    def process_item(self, item, spider):
        if "dogetipbot" == spider.name:
            thread = item.get("thread", None)

            if not thread:
                raise DropItem("Empty thread")

        return item

