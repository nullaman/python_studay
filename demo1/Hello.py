# -*- coding: utf-8 -*-
# @Time : 2021/10/19 9:34
# @Author : AMan

print("Hello World")
print('Hello Aman')

# fp = open("/demo1/testFile/testFP.txt", "a+")
fp = open("D:/OpenSource_Python/demo1/testFile/testFP.txt", "a+")

print("aaaaa", file=fp)
print("为什么中文不出来，且为GBK", file=fp)
fp.close()
