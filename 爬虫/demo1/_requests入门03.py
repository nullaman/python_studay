# -*- coding: utf-8 -*-
# @Time : 2022/5/24 9:40
# @Author : AMan

import requests

url = 'https://movie.douban.com/j/chart/top_list'

param = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

hd = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

resp = requests.get(url=url, params=param, headers=hd)
print(resp.request.url)
print(resp.request.headers)

print(resp.text)
print(resp.json()[0])

resp.close()
