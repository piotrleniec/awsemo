import scrapy


class AwsemoSpider(scrapy.Spider):
    name = "awsemo"
    start_urls = ['https://github.com/sindresorhus/awesome']

    def parse(self, response):
        for url in response.css('#readme a::attr(href)').extract():
            self.log(url + '/n')
