# -*- coding: utf-8 -*-
# @Time : 2022/5/24 14:39
# @Author : AMan

import requests
import re
import csv

url = "https://movie.douban.com/chart"
heds = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

# 获取网页源代码
codeUrlText = requests.get(url=url, headers=heds).text
# print(codeUrl)

# 正则匹配
com = re.compile(
    r'<table width="100%" class="">.*?<tr class="item">.*?<td width="100" valign="top">.*?<div class="pl2">.*?<a href="(?P<mUrl>.*?)"  class="">(?P<mName>.*?)/ <span style="font-size:13px;">.*?<p class="pl">(?P<mYear>.*?)/.*?<span class="rating_nums">(?P<mSoure>.*?)</span>.*?<span class="pl">\((?P<mPeople>.*?)\)</span>.*?</div>.*?</div>.*?</td>.*?</tr>.*?</table>',
    re.S)
# 匹配数据
iters = com.finditer(codeUrlText)

# 写入csv准备
f = open("data.csv", mode="w", encoding="utf-8")
csvWriter = csv.writer(f)

# 开始写入
for i in iters:
    # print(i.group())
    # print("-------------------------------")
    # print(i.group("mUrl"))
    # print(i.group("mName").strip())
    # print(i.group("mYear"))
    # print(i.group("mSoure"))
    # print(i.group("mPeople"))
    # print("-------------------------------")

    dic = i.groupdict()
    dic["mName"] = dic["mName"].strip()
    csvWriter.writerow(dic.values())

f.close()
print("over")
