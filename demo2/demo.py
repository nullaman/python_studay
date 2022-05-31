# -*- coding: utf-8 -*-
# @Time : 2021/10/19 12:11
# @Author : AMan
r = range(10)
print(r)
print(list(r))

r2 = range(1, 10)
print(r2)
print(list(r2))

r3 = range(1, 10, 3)
print(r3)
print(list(r3))

a = 0
sum = 0
while a < 5:
    sum += a
    a += 1
print(sum)

print('------------1-100 偶数---------')
allSum = 0
a = 1
while a <= 100:
    if a % 2 == 0:
        allSum += a
    a += 1
print(allSum)

for item in 'wocao':
    print(item)

for i in range(10):
    print(i)

for _ in range(10):
    print(1111111111111)

