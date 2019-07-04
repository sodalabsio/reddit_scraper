# -*- coding: utf-8 -*-

# Scrapy settings for reddit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'reddit'

SPIDER_MODULES = ['reddit.spiders']
NEWSPIDER_MODULE = 'reddit.spiders'

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 408, 429, 301, 303]
# Maximum number of times to retry, in addition to the first download.
RETRY_TIMES = 100

DOWNLOAD_DELAY = 50 

PROXY = 'http://localhost:8118'

DOWNLOADER_MIDDLEWARES = {
    'reddit.middlewares.RandomUserAgentMiddleware': 400,
    'reddit.middlewares.ProxyMiddleware': 410,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None
}

ITEM_PIPELINES = {
    'reddit.pipelines.RedditPipeline': 5
}

FEED_EXPORTERS = {
    'csv': 'reddit.feedexport.CSVkwItemExporter',
    'csv-comment': 'reddit.feedexport.CSVkwCommentItemExporter'
}

# By specifying the fields to export, the CSV export honors the order
# rather than using a random order.
EXPORT_FIELDS = [
#    "url",
    "thread",
    "op",
    "subreddit",
    "date",
    "time",
    "sender",
    "receiver",
    "dogecoin",
    "usd"
]

COMMENT_EXPORT_FIELDS = [
    "url",
    "thread",
    "op",
    "thread_date",
    "textpost",
    "comments",
    "vote_points",
    "upvoted",
    "comment",
    "user",
    "time"
]

# Delimiter for csv file
CSV_DELIMITER = ','

