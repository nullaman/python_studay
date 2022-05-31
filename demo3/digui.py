# -*- coding: utf-8 -*-
# @Time : 2022/5/19 15:55
# @Author : AMan

def digui(a):
    if a == 1:
        return 1
    else:
        return a * digui(a - 1)


print(digui(6))
