import scrapy


class WenzhouSpider(scrapy.Spider):
    name = 'wenzhou'
    allowed_domains = ['http://www.wzair.cn/lkfw/hbxx/jrdg/index.html?v=1606439135598']
    start_urls = ['http://http://www.wzair.cn/lkfw/hbxx/jrdg/index.html?v=1606439135598/']

    def parse(self, response):
        pass
