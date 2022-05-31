# -*- coding: utf-8 -*-
# @Time : 2021/10/19 16:22
# @Author : AMan

list = [1, 1, 12, 324, 2]
print(list)
print(id(list))
list.append('111')
print(list)
print(id(list))

list3 = list[::]

list2 = ["add", '哈哈哈']
list.append(list2)
print(list)
list3.extend(list2)
print(list3)

list3.insert(1, "插入")
print(list3)

list3[1:3] = ['插入和1被我顶了']
print(list3 )
