# -*- coding: utf-8 -*-
# @Time : 2022/5/24 9:59
# @Author : AMan


import requests

url = "https://fanyi.baidu.com/sug"
i = input("输入要翻译的英文")
dat = {
    "kw": i
}
resp = requests.post(url, data=dat)

j = resp.json()
print(j)
print(j.get("data"))
print("--------")

for v in j.get("data"):
    print(v.get("v"))

resp.close()