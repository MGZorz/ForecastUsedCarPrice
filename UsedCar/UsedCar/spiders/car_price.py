# -*- coding: utf-8 -*-
import re

import scrapy
from UsedCar.items import UsedcarItem


class CarPriceSpider(scrapy.Spider):
    name = 'car_price'
    allowed_domains = ['bj.58.com']
    url_tempalte = 'https://bj.58.com/ershouche/pn{page}/'

    # start_urls = [url_tempalte.format(1)]

    def start_requests(self):
        for page in range(1, 50):
            url = self.url_tempalte.format(page=page)
            print(url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        lis = response.xpath('//li[@class="clearfix car_list_less"]')
        for li in lis:
            item = UsedcarItem()
            item['brand'] = li.css(".info_tit").xpath(".//font/text()").get()
            item['title'] = re.compile("</font>(.*?)</h1>").findall(li.get())[0]
            info = li.css(".info_param").xpath(".//span/text()").getall()
            item['start_time'] = info[0]
            item['distance'] = info[1]
            item['fuel'] = info[2]
            item['gear'] = info[3]
            item['tag'] = "_".join(li.css(".tags_left").xpath(".//em/text()").getall())
            item['price'] = li.xpath(".//div[@class='col col3']/h3/text()").get()
            # print(item)
            yield item
