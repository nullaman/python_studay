# -*- coding: utf-8 -*-
# @Time : 2022/5/20 11:00
# @Author : AMan


class Student:
    native_pace = "江西"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃吃吃。。。" + self.name)

    @staticmethod
    def method():
        print("静态方法")

    @classmethod
    def cm(cls):
        print('类方法')


def drink():
    print('喝水...')


st1 = Student('caoxiang', 100)
st1.cm()
st1.eat()
drink()

Student.eat(st1)
