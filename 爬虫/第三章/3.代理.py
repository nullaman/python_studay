# -*- coding: utf-8 -*-
# @Time : 2022/5/25 16:56
# @Author : AMan

import requests

# 222.65.228.96:8085 HTTP
proxies = {
    # 看需要访问的网站是否带s
    # 'http' : ''
    'https': 'https://dd001.zhuan666.top:11606'
}

url = 'https://www.baidu.com/'
resp = requests.get(url, proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
