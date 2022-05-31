# -*- coding: utf-8 -*-
# @Time : 2021/10/19 15:59
# @Author : AMan

list1 = [1, '2', '哈哈哈']
list2 = [1, '2', '哈哈哈']
print(id(list1), type(list1), list1)
print(id(list2), type(list2), list2)
print(list1 == list2)
print(list1 is list2)

print(list1[0], list1[2])
for i in list1:
    print(i)
print(1 in list1)

print('--------------------')

print(list1.index(1))
# print(list1.index(111111))  # 异常
print(list1[-1])

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4 = list3[1:3]
print(list4)
list5 = list3[1:8:2]
print(list5)
