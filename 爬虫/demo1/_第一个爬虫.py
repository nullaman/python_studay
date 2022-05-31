# -*- coding: utf-8 -*-
# @Time : 2022/5/23 17:28
# @Author : AMan

from urllib.request import urlopen

url = 'https://www.baidu.com/'
resp = urlopen(url)

# 读取到网页的源代码
str = resp.read().decode('utf-8')

print(str)

with open('mybaidu.html', mode='w') as f:
    f.write(str)
