# -*- coding: utf-8 -*-
# @Time : 2022/5/26 15:09
# @Author : AMan

import requests
import csv
from concurrent.futures import ThreadPoolExecutor
import time

f = open("data.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)


def download_one_page(page_index):
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    page_size = 20
    data = {
        "limit": page_size,
        "current": page_index
    }
    resp = requests.post(url=url, data=data)
    list = resp.json().get("list")
    print(list)
    for i in list:
        prodName = i.get("prodName")
        prodCat = i.get("prodCat")
        lowPrice = i.get("lowPrice")
        highPrice = i.get("highPrice")
        avgPrice = i.get("avgPrice")
        place = i.get("place")
        unitInfo = i.get("unitInfo")
        pubDate = i.get("pubDate")
        text = [prodName, prodCat, lowPrice, highPrice, avgPrice, place, unitInfo, pubDate]
        csv_writer.writerow(text)

    print("完成页码：", page_index)


if __name__ == '__main__':
    # 爬取一页数据
    # page_index = 1
    # download_one_page(page_index)
    # 多线程爬取
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 11):  # range(1, 15664 ):
            t.submit(download_one_page, page_index=i)

    print("over~")
