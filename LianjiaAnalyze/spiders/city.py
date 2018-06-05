import scrapy


class CitySpider(scrapy.Spider):
    name = "city"

    def start_requests(self):
        urls = [
            'https://www.lianjia.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for title in response.css('ul.clear'):
            yield {
                'city': title.css('li.a::text').extract_first()
            }
