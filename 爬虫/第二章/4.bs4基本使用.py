# -*- coding: utf-8 -*-
# @Time : 2022/5/24 17:41
# @Author : AMan

import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/index.html"
resp = requests.get(url)
code = resp.text
# print(code)
page = BeautifulSoup(code, "html.parser")  # 指定html解析器
# find(标签，属性=值)
# find_all(标签，属性=值)
table = page.find("div", class_='tbl-body')
# table = page.find("div", attrs={"class": "tbl-body"})
trs = table.find_all("tr")
# print(trs)
for tr in trs:
    ths = tr.find_all("th")
    print(ths[0].text)
    print(ths[1].text)
    print(ths[2].text)
    print(ths[3].text)
    print(ths[4].text)
    print(ths[5].text)
    print(ths[6].text)
    print(ths[7].text)

# 数据接口
dataUrl = "http://www.xinfadi.com.cn/getCat.html"
data = {
    "prodCatid": 1186
}
resp2 = requests.post(url=dataUrl, data=data)
# print(resp2.json())
for i in resp2.json().get("list"):
    print(i)
