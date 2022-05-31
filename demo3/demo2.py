# -*- coding: utf-8 -*-
# @Time : 2021/11/4 10:49
# @Author : AMan

def fun(a1, a2):
    print(a1)
    print(a2)
    a1 = 100
    a2.append(10)
    print(a1)
    print(a2)


a = 10
b = [11, 22, 33]
print(a)
print(b)
print('-------------')
fun(a, b)
print('-------------')
print(a)
print(b)

print('%.9f' % 3.141592653)


def aman(*args):
    print(args)


aman(1, 2, 3)


def aman2(**args):
    print(args.get('a'))
    print(args)


aman2(a=1, b=2, c=3)
