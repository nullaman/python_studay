# -*- coding: utf-8 -*-
# @Time : 2021/10/20 15:59
# @Author : AMan


t1 = ('1234', 'ahh哈哈', 98)
print(type(t1))
t2 = '1234', 'ahh哈哈', 98
print(type(t2))
t3 = '234'
print(type(t3))


t4 = tuple(('1234', 'ahh哈哈', 98))
print(type(t4))

tt = tuple(('1234', 98, [11, 22, 33]))
print(type(tt))
print(tt)
print(tt[0], type(tt[0]), id(tt[0]))
print(tt[1], type(tt[1]), id(tt[1]))
print(tt[2], type(tt[2]), id(tt[2]))

tt[2].append('加')
print(tt)
