import scrapy
from scrapy.http import Request
from urllib import parse

class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['https://readhub.cn/topics']
    base_url = 'https://readhub.cn'

    def parse(self, response):
        # 解析列表中的所有文章url并交给scrapy下载后并进行解析
        post_urls = response.css('.topicItem___1B0j1 .topicTitle___1HWIA a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并交给scrapy下载

    def parse_detail(self, response):
        # 提取文章的具体字段
        # xpath 方式匹配
        re_selector = response.xpath('/html/head/title/text()')
        # css 方式匹配
        re_selector_css = response.css('title::text').extract_first()
        pass
