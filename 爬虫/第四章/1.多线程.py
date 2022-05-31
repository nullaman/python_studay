# -*- coding: utf-8 -*-
# @Time : 2022/5/26 11:56
# @Author : AMan

from threading import Thread


# 写法1
# def func():
#     for i in range(1000):
#         print("func:", i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)
#     t.start()
#     for i in range(1000):
#         print("main:", i)


# 写法2
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程:", i)
#
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#     for i in range(1000):
#         print("主线程:", i)

# 写法1 传参
def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t = Thread(target=func, args=("周杰伦",))
    t.start()

    t2 = Thread(target=func, args=("林俊杰",))
    t2.start()
