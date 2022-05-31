# -*- coding: utf-8 -*-
# @Time : 2021/10/20 17:42
# @Author : AMan

s = 'wo shi cao xiang'
print(s.split())

s2 = 'ni|shi|na|wei'
print(s2.split('|'))
print(s2.split('|', 1))

print(s2.rsplit('|', 1))
