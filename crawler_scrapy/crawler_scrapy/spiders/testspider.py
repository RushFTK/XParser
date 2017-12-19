import scrapy

class testspider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://tester1.409dostastudio.work/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'test-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(responsebody)
        self.log('Saved file %s' % filename)
