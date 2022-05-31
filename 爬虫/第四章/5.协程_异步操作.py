# -*- coding: utf-8 -*-
# @Time : 2022/5/26 16:06
# @Author : AMan

# input(） 程序也是处于阻塞状态
# requests. get (bilibili） 在网络请求返回数据之前，程序也是处于阻塞状态的
# 一般情况下，当程序处于 IO操作的时候。线程都会处于阻塞状态
# 协程：当程序遇见了I0操作的时候。可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换。切换条件一般就是I0操作
# 在宏观上，我们能看到的其实是多个任务一起在执行
# 多任务异步操作
# 上方所讲的一切。都是在单线程的条件下瓦

import asyncio
import time


# async def func():
#     print("hello,python")
#
#
# if __name__ == '__main__':
#     a = func()  # 此时的函数是异步协程函数，得到的是一个协程对象
#     asyncio.run(a)  # 协程程序运行需要asyncio模块的支持

async def func1():
    print("hello,func1")
    # time.sleep(1)
    await asyncio.sleep(1)
    print("hello,func1")


async def func2():
    print("hello,func2")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("hello,func2")


async def func3():
    print("hello,func3")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("hello,func3")


async def func4():
    print("hello,func3")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("hello,func3")


# 写法
# if __name__ == '__main__':
#     begin = time.time()
#     a1 = func1()
#     a2 = func2()
#     a3 = func3()
#     a4 = func4()
#     tasks = [
#         a1, a2, a3, a4
#     ]
#     # 一次多个给wait执行
#     asyncio.run(asyncio.wait(tasks))
#     end = time.time()
#     print(end - begin)

# 推荐写法：
async def main():
    # 第一种写法
    # f1 = func1()
    # await f1  # await挂起操作放在协程对象前面

    # 推荐写法
    tasks = [
        # func1(),
        # func2(),
        # func3(),
        # func4()
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
        asyncio.create_task(func4())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    begin = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - begin)
