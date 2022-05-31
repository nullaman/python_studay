# -*- coding: utf-8 -*-
# @Time : 2022/5/25 14:57
# @Author : AMan

import requests
from lxml import etree
import time

url = "https://guangzhou.zbj.com/search/f/?kw=saas"
resp = requests.get(url)
codeUrl = resp.text
# print(codeUrl)


tree = etree.HTML(codeUrl)
# print(tree)
# 获取到列表
divs = tree.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
print(divs)
for d in divs:
    # ['¥1918', '近半年成交：182笔', '保证完成']
    # print(d.xpath("./div//div[@class='service-info-wrap']//span/text()"))
    fuwu = d.xpath(".//p[@class='title']/text()")[0]
    price = d.xpath(".//span[@class='price']/text()")[0].strip('¥')
    chengjiao = d.xpath(".//span[@class='amount']/text()")[0]
    print("服务名称:" + fuwu + "\t价格:" + price + "\t" + chengjiao)

print('---over---')
