# -*- coding: utf-8 -*-
#import scrapy
from scrapy import Spider
from scrapy.http import FormRequest 
from scrapy.utils.response import open_in_browser
from scrapy.http import Request
from scrapy.shell import inspect_response

downloadurl = \
'https://elearning.physik.uni-frankfurt.de/goto_FB13-PhysikOnline_file_21311_download.html'

filename = 'test.pdf'


class ElearningSpider(Spider):

    name = 'elearning'
    allowed_domains = ['elearning.physik.uni-frankfurt.de']
    start_urls = ['http://elearning.physik.uni-frankfurt.de/login.php']

    def parse(self, response):
        return FormRequest.from_response(response,
                                         formdata={'username': 'foo',
                                                   'password': 'bar'},
                                         callback=self.scrapepages)
    
    def scrapepages(self, response):
        yield Request(downloadurl, callback=self.save_pdf)

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(filename, 'wb') as f:
            f.write(response.body)
