# -*- coding: utf-8 -*-
# @Time : 2022/5/24 15:30
# @Author : AMan

import requests
import re

domain = "https://dytt89.com/"

# verify=False 解决错误SSLError, 去掉安全验证
rep = requests.get(domain, verify=False)
# 页面编码有 charset=gb2312
rep.encoding = 'gb2312'

paperCode = rep.text
# print(paperCode)

# 拿到表单ul
obj1 = re.compile('2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
result1 = obj1.finditer(paperCode)

list = []
for r1 in result1:
    ul = r1.group("ul")
    # print(ul)

    obj2 = re.compile("<a href='/(?P<href>.*?)'")
    result2 = obj2.finditer(ul)
    for r2 in result2:
        href = r2.group("href")
        # print(domain + href)
        list.append(domain + href)

for u in list:
    # print(u)
    resp = requests.get(u)
    resp.encoding = 'gb2312'
    paperCode = resp.text
    # print(paperCode)
    obj = re.compile(
        '【下载地址】本站专属下载器：点击下方链接 即可享受高速下载和在线播放 专治迅雷无法下载.*?<li><a href="(?P<url1>.*?)">.*?【下载地址】magnet推荐使用utorrent、BitComet等bt客户端下载.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<url2>.*?)">',
        re.S)
    result = obj.finditer(paperCode)
    for r in result:
        print(r.group("url1"))
        print(r.group("url2"))
        print("-------------------")
