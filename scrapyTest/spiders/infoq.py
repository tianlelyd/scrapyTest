import scrapy


class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['https://www.infoq.cn/theme/85']

    def parse(self, response):
        re_selector = response.xpath('/html/head/title/text()')
        pass
