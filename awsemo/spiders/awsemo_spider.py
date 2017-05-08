import scrapy


class AwsemoSpider(scrapy.Spider):
    name = "awsemo"
    start_urls = ['https://github.com/sindresorhus/awesome']

    def parse(self, response):
        for link in response.css('div.readme a::attr(href)').extract():
            self.log(link + '/n')
