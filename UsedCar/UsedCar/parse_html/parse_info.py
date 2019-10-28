import re

from scrapy import Selector

file = open('li.html', 'r', encoding='utf-8')
context = file.read()
li = Selector(text=context)
brand = li.css('.info_tit').xpath('.//font/text()').get()
title = re.compile("</font>(.*?)\n").findall(li.get())[0]
info = li.css(".info_param").xpath(".//span/text()").getall()
start_time = info[0]
distance = info[1]
volumn = info[2]
gear = info[3]
tag = "_".join(li.css(".tags_left").xpath(".//em[@class='emShow']/text()").getall())
price = li.xpath(".//div[@class='col col3']/h3/text()").get()
print(title)
# print(brand, title, start_time, distance, volumn, gear, tag, price)
