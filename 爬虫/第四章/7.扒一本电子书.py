# -*- coding: utf-8 -*-
# @Time : 2022/5/26 17:58
# @Author : AMan

import requests
import aiohttp
import asyncio
import aiofiles


def get_catalog_list(book_id):
    get_catalog_url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%22' + book_id + '%22}'
    resp = requests.get(get_catalog_url)
    catalog_list = resp.json()["data"]["novel"]["items"]
    return catalog_list


async def get_content(book_id, c_id, title):
    file_name = '小说/' + title + '.txt'
    get_chapter_content_url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%22' + book_id + '%22,%22cid%22:%22' + book_id + '|' + c_id + '%22,%22need_bookinfo%22:1}'
    async with aiohttp.ClientSession() as session:
        async with session.get(get_chapter_content_url) as resp:
            result = await resp.json()
            async with aiofiles.open(file_name, mode='w', encoding='utf-8') as f:
                await f.write(result['data']['novel']['content'])
                print(title, "--- 完成！")
                # author = json['data']['novel']['author']
                # chapter_title = json['data']['novel']['chapter_title']


async def main():
    tasks = []
    # 西游记
    book_id = '4306063500'
    catalog_list = get_catalog_list(book_id)
    for catalog in catalog_list:
        c_id = catalog['cid']
        title = catalog['title']
        tasks.append(asyncio.create_task(get_content(book_id, c_id, title)))
    await asyncio.wait(tasks)
    print("--- over！ ---")


if __name__ == '__main__':
    # 会报错，不知道为什么
    # asyncio.run(main())
    # 百度说使用下面这个，确实解决了
    asyncio.get_event_loop().run_until_complete(main())
