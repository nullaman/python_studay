# -*- coding: utf-8 -*-
# @Time : 2021/10/19 10:59
# @Author : AMan

a = 10
b = 20
print(a == b)
print(a is b)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)

print('------------------------')
c, d = 1, 2
print(c == 1 and d == 2)
print(c == 1 or d == 2)

# not 对Boolean取反
f = True
print(not f)

# in 和 not in ，存在，是否存在
s = " aaa bbb"
print('a' in s)
print('b' not in s)
