# -*- coding: utf-8 -*-
# @Time : 2022/5/24 9:40
# @Author : AMan

import requests

query = input("请输入你要搜索的")

url = f'https://www.sogou.com/web?query={query}'
# 处理反爬，没有headers就会报错
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

resp = requests.get(url, headers=dic)
print(resp)
print('--------------------------------------- ')
print(resp.text)

resp.close()