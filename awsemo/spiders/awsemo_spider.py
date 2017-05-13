import scrapy


class AwsemoSpider(scrapy.Spider):
    name = "awsemo"
    start_urls = ['https://github.com/sindresorhus/awesome']

    def parse(self, response):
        for u in response.css('#readme a::attr(href)').extract():
            yield {'url': u}
