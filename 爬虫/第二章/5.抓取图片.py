# -*- coding: utf-8 -*-
# @Time : 2022/5/25 11:34
# @Author : AMan

import requests
from bs4 import BeautifulSoup
import re
import time

url = "https://www.umeitu.com/bizhitupian/fengjingbizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"
code = resp.text
# print(code)

page = BeautifulSoup(code, "html.parser")
ul = page.find("ul", class_="pic-list after")
# print(ul)
alist = ul.find_all("a")
# print(alist)

url = "https://www.umeitu.com"

for a in alist:
    # print(url + a.get("href"))
    aresp = requests.get(url + a.get("href"))
    aresp.encoding = "utf-8"
    acode = aresp.text
    # print(acode)

    apage = BeautifulSoup(acode, "html.parser")
    se = apage.find("section", class_="img-content")
    imgContent = se.find("img")

    imageName = imgContent.get("alt")
    imageUrl = imgContent.get("src")
    print(imageName + ":" + imageUrl)

    img_resp = requests.get(imageUrl)

    downloadName = imageName + "." + imageUrl.split("/")[-1].split(".")[-1]
    print(downloadName)

    with open("img/" + downloadName, mode='wb') as f:
        f.write(img_resp.content)
    print("over_________")
    time.sleep(2)
