# -*- coding: utf-8 -*-
# @Time : 2021/10/19 11:24
# @Author : AMan

money = 1000
s = int(input('取钱多少\n'))
if money >= s:
    money = money - s
    print('取款' + str(s) + ',余额' + str(money))
else:
    print('你只有' + str(money) + '钱')

n = int(input("输入一个整数"))
if n % 2 == 0:
    print(n, '偶数')
else:
    print(n, '奇数')

m = int(input("输入一个整数"))
if m == 0:
    print(m, '是零')
elif m >= 90:
    print("A")
elif m >= 70 and m < 90:
    print("B")
elif 40 > m > 30:
    print("C")
else:
    print("D")

print('傻逼' if m == 1 else "天才")

if m == 1:
    print("测试")
