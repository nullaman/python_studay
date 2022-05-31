# -*- coding: utf-8 -*-
# @Time : 2021/10/20 15:01
# @Author : AMan

scores = {'张三': 100, '李四': 55, 'aman': 1000099}
scores['张三'] = 1

keys = scores.keys()
print(keys)

vs = scores.values();
print(vs)

zs = scores.get("张三")
print(zs)

its = scores.items()
print(its)

for it in scores:
    print(it, scores[it], scores.get(it))
