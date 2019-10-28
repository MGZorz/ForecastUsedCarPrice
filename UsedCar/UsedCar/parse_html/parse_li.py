from scrapy import Selector

# 使用Scrapy中的选择器分析页面
context = open('t.html', 'r', encoding='utf-8')
selector = Selector(text=context.read())
lis = selector.xpath('.//li[@class="clearfix car_list_less"]')
print(len(lis))
