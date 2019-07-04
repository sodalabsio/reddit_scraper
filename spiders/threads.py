# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from reddit.items import CommentItem
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst, Compose, Join, Identity
from reddit import utils


def get_comments_count(x):
    return utils.regex_extractor(r"(.*)\s+comment.*", x, 1)


def get_upvoted(x):
    return utils.regex_extractor(r"\((.*)\s+upvoted", x, 1)


class CommentItemLoader(ItemLoader):
    default_item_class = CommentItem
    default_input_processor = MapCompose(lambda x: x.strip())
    default_output_processor = Compose(TakeFirst(), lambda x: x.strip())
    default_selector_class = Selector
    textpost_out = Compose(Join(" "), lambda x: x.strip())
    comments_out = Compose(TakeFirst(), get_comments_count, lambda x: x.strip())
    upvoted_out = Compose(TakeFirst(), get_upvoted, lambda x: x.strip())
    comment_out = Compose(Join(" "), lambda x: x.strip())



class ThreadsSpider(CrawlSpider):
    name = "threads"
    allowed_domains = ["reddit.com"]
    start_urls = (
        "https://www.reddit.com/r/",  #Enter Reddit thread here
    )

    rules = (
        Rule(LinkExtractor(restrict_xpaths=(".//div[@class='nav-buttons']")), follow=True),
        Rule(LinkExtractor(restrict_xpaths=(".//div[@class='content']//p[@class='parent']/a[@class='title']")), callback="parse_item"),
    )


    def parse_item(self, response):
        hxs = Selector(response)

        thread = hxs.xpath(".//p[@class='title']/a/text()").extract()
        op = hxs.xpath(".//div[contains(@class, 'self')]//p[@class='tagline']/a[contains(@class, 'author')]/text()").extract()
        thread_date = hxs.xpath(".//div[contains(@class, 'self')]//p[@class='tagline']/time/@title").extract()
        textpost = hxs.xpath(".//div[contains(@class, 'self')]//div[@class='md']//text()").extract()
        comments = hxs.xpath(".//div[contains(@class, 'self')]//a[contains(@class, 'comments')]/text()").extract()
        vote_points = hxs.xpath(".//div[@class='linkinfo']/div[@class='score']/span[@class='number']/text()").extract()
        upvoted = hxs.xpath(".//div[@class='linkinfo']/div[@class='score']/text()").extract()

        rows = hxs.xpath(".//div[@class='commentarea']//div[contains(@class, 'comment')]/div[contains(@class, 'entry')]")
        for row in rows:
            l = CommentItemLoader(item = CommentItem(), response = response)
            l.add_value("url", response.url)
            l.add_value("thread", thread)
            l.add_value("op", op)
            l.add_value("thread_date", thread_date)
            l.add_value("textpost", textpost)
            l.add_value("comments", comments)
            l.add_value("vote_points", vote_points)
            l.add_value("upvoted", upvoted)
            l.add_value("comment", row.xpath(".//div[contains(@class, 'usertext-body')]//text()").extract())
            l.add_value("user", row.xpath(".//p[@class='tagline']/a[contains(@class, 'author')]/text()").extract())
            l.add_value("time", row.xpath(".//p[@class='tagline']/time/@title").extract())

            yield l.load_item()
