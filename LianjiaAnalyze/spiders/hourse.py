import scrapy


class QuotesSpider(scrapy.Spider):
    name = "hourses"

    def start_requests(self):
        urls = [
            'https://sh.lianjia.com/ershoufang/pudong/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('clear.title'):
            yield {
                'href': a.css('href::text').extract_first()
            }