# -*- coding: utf-8 -*-
# @Time : 2022/5/26 16:56
# @Author : AMan

# request.get() 同步代码 -> 异步操作aiohttp   pip install aiohttp

import aiohttp
import asyncio

urls = [
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/zlsocudgy4y.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/qg0y3bao5se.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/tfm5ffgjf43.jpg"
]


async def download_img(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())
    print("over!", name)


async def main():
    tasks = []
    for url in urls:
        tasks.append(download_img(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
