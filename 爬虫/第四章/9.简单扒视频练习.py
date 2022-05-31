# -*- coding: utf-8 -*-
# @Time : 2022/5/27 13:08
# @Author : AMan

"""
流程:
1.拿到548121-1-1.html的页面源代码
2.从源代码中提取到m3u8的url
3.下载m3u8
4.读取m3u8文件，下载视频
5.合并视频
"""

import requests
import re


def download_mu38():
    html_url = 'https://91kanju.com/vod-play/59780-1-2.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    }
    resp = requests.get(html_url, headers=headers)
    resp.encoding = 'utf-8'
    html_code = resp.text
    # print(html_code)
    obj = re.compile("video: {.*?url: '(?P<m3u8_url>.*?)',", re.S)
    m3u8_url = obj.search(html_code).group("m3u8_url")
    print(m3u8_url)
    resp.close()

    resp = requests.get(m3u8_url, headers=headers)
    resp.encoding = 'utf-8'
    m3u8_code = resp.text
    print(m3u8_code)

    with open("完美世界02.m3u8", mode='w') as f:
        f.write(m3u8_code)

    resp.close()
    print('over~')


def download_video():
    n = 1
    with open("完美世界02.m3u8", mode='r') as f:
        for line in f:
            line = line.strip()
            # 过滤没有用的
            if line.startswith("#"):
                continue

            # 下载视频
            resp = requests.get(line)
            with open(f"视频/{n}.ts", mode='wb') as v:
                v.write(resp.content)
            resp.close()
            n += 1
            print('完成:', line)


if __name__ == '__main__':
    # 下载mu38到本地
    download_mu38()
    download_video()
