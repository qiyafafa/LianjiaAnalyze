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
        for ul in response.css('ul.clear'):
            city_names = ul.xpath('li/a/text()').extract()
            city_urls = ul.xpath('li/a/@href').extract()
            for i in range(0, len(city_names)):
            	yield {
	     		'city':    city_names[i],
	     		'city_url': city_urls[i]
            	}
