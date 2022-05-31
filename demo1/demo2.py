# -*- coding: utf-8 -*-
# @Time : 2021/10/19 9:59
# @Author : AMan
import keyword

# python中的保留字
print(keyword.kwlist)
# 'False', 'None', 'True', '__peg_parser__', 'and',
# 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from',
# 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield'
age = 18
name = '张三'
# print('我是' + name + '今年' + age)
print('我是' + name + '今年' + str(age))
