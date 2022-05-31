# -*- coding: utf-8 -*-
# @Time : 2022/5/26 14:44
# @Author : AMan

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(1000):
        print("name:", name, "range", i)


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")
    print("over")
