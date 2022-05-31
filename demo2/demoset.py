# -*- coding: utf-8 -*-
# @Time : 2021/10/20 16:19
# @Author : AMan

ss = {1, 1, 3, 3, 4, 5, 6}
print(ss)
print(type(ss))

s2 = {'python'}
print(s2)

s3 = set('python')
print(s3)

s4 = set({1, 5, 4, 6, 7, 20})
print(s4)

s4.add('cao')
print(s4)
print("------------------")
s4.update([1, '哈哈哈'])
print(s4)

s4.update({'duduud', 99})
print(s4)

s4.update(('真牛', 66666))
print(s4)

s4.remove(1)
print(s4)

s4.discard("????")
print(s4)
s4.discard("哈哈哈")
print(s4)

ss1 = {1, 1, 3, 3, 4, 5, 6}
ss2 = {1, 3, 4, 5, 6}
print(ss1, id(ss1))
print(ss2, id(ss2))
print(ss1 == ss2)
print(ss1 is ss2)
print('------------------------------')
sss1 = {1, 3, 4, 5, 6}
sss2 = {1, 3, 4}
sss3 = {1, 3, 100}
sss4 = {'啥玩意'}
print(sss2.issubset(sss1))
print(sss3.issubset(sss1))
print('------------------------------')

print(sss1.issuperset(sss2), ">>")
print(sss1.issuperset(sss3))
print('------------------------------')

print(sss1.isdisjoint(sss2))
print(sss1.isdisjoint(sss3))
print('------------------------------')
print(sss1.isdisjoint(sss4))