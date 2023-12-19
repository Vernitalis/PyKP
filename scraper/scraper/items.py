# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StationItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    key = scrapy.Field()
    iso = scrapy.Field()
    nz = scrapy.Field()

class CredentialsItem(scrapy.Item):
    header_token = scrapy.Field()
    body_token = scrapy.Field()
    headers = scrapy.Field()
