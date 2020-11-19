import scrapy


class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['https://www.infoq.cn/article/DBSU7KiLwhyR8rUpBIT9']

    def parse(self, response):
        # xpath 方式匹配
        re_selector = response.xpath('/html/head/title/text()')
        # css 方式匹配
        re_selector_css = response.css('title::text').extract_first()
        pass
