# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # tags = scrapy.Field()
    # borndate = scrapy.Field()
    # description = scrapy.Field()
    # bornlocation = scrapy.Field()
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        self._values[key] = value
        super().__setitem__(key, value)