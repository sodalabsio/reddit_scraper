# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DogeTipBotItem(scrapy.Item):
    url = scrapy.Field()
    thread = scrapy.Field()
    op = scrapy.Field()
    subreddit = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    sender = scrapy.Field()
    receiver = scrapy.Field()
    dogecoin = scrapy.Field()
    usd = scrapy.Field()


class CommentItem(scrapy.Item):
    url = scrapy.Field()
    thread = scrapy.Field()
    op = scrapy.Field()
    thread_date = scrapy.Field()
    textpost = scrapy.Field()
    comments = scrapy.Field()
    vote_points = scrapy.Field()
    upvoted = scrapy.Field()
    comment = scrapy.Field()
    user = scrapy.Field()
    time = scrapy.Field()

