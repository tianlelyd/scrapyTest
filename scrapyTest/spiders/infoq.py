import scrapy


class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['http://www.infoq.cn/']

    def parse(self, response):
        pass
