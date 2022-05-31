# -*- coding: utf-8 -*-
# @Time : 2021/10/19 10:37
# @Author : AMan

print(1 + 1)
print(1 - 1)
print(2 * 3)
print(2 / 4)
# 取整数
print(5 // 3)
# 取余数
print(10 % 3)
# 幂次方 2的三次方
print(2 ** 3)

print('---------------- ')

print(9 // 4)  # 2
print(-9 // -4)  # 2

# 一正一负 向下取整
print(9 // -4)  # -2.25 ---> -3
print(-9 // 4)  # -2.25 ---> -3

# 一正一负：余数=被除数-除数*商
print(9 % -4)  # 9-（-4）*（-3） = -3
print(-9 % 4)  # -9-4*（-3）= 3


# 交换
a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)