# -*- coding: utf-8 -*-
# @Time : 2022/5/24 11:53
# @Author : AMan

import re

s = "我的电话是10086，女朋友是10010"
rh = "\d+"

# 返回列表
lst = re.findall("\d+", s)
print(lst)

# 返回迭代器
ite = re.finditer(r"\d+", s)
for i in ite:
    print(i.group())

se = re.search(r"\d", s)
# 找到一个就返回
print(se.group())

# 预加载正则
obj = re.compile(r"\d+")
reit = obj.finditer(s)
for i in reit:
    print(i.group())

s = """
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='aman'><span id='2'>阿瞒</span></div>
<div class='yjc'><span id='3'>易嘉c</span></div>
<div class='wp'><span id='4'>王p</span></div>
"""

# re.S让.可以匹配换行符
obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)
result = obj.finditer(s)
for i in result:
    print(i.group())

# (?P<分钟名字>正则)，可以提取指定分组的内容
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<hahah>.*?)</span></div>", re.S)
result = obj.finditer(s)
for i in result:
    print(i.group("hahah"))
