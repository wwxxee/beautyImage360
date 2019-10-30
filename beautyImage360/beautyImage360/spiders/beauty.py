# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json

from beautyImage360.items import Image360Item

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {'ch': 'beauty', 'listtype': 'new'}
        base_url = "https://image.so.com/zjl?"
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Image360Item()
            item['id'] = image.get('id')
            item['title'] = image.get('title')
            item['purl'] = image.get('purl')
            item['qhimg_downurl'] = image.get('qhimg_downurl')
            yield item

