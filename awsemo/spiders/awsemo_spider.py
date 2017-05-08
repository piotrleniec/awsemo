import scrapy


class AwsemoSpider(scrapy.Spider):
    name = "awsemo"
    start_urls = ['https://github.com/sindresorhus/awesome']

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = '{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))
