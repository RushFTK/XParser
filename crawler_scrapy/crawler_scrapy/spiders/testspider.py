import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
class testspider(scrapy.Spider):
    name = "test"
    start_urls = ['http://tester1.409dostastudio.work/'
                  ]
                  # ,'http://tester2.409dostastudio.work/']

    def parse(self, response):
        #get all request page
        urls = response.xpath('//@href').extract()
        for path_url in urls:
             self.log('Get url - %s' % path_url)
             yield Request(response.url + path_url.split[1], callback=self.parseContent)

        #save pages
        page = response.url
        filename = 'test-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    #get context
    def parseContent(self, response):
        pass