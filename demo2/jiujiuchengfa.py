# -*- coding: utf-8 -*-
# @Time : 2021/10/19 15:36
# @Author : AMan

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()