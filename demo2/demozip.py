# -*- coding: utf-8 -*-
# @Time : 2021/10/20 15:15
# @Author : AMan

name = ['zs', 'ls', 'ww']
sc = [234, 4532, 1234]

nc = {name: sc for name, sc in zip(name, sc)}
print(nc)

