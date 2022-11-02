import scrapy


class AsinspiderSpider(scrapy.Spider):
    name = 'asinspider'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
