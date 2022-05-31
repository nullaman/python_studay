# -*- coding: utf-8 -*-
# @Time : 2022/5/25 16:25
# @Author : AMan

import requests

url = 'https://www.pearvideo.com/video_1763224'
videoId = url.split('_')[1]
# print(videoId)
v_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + videoId + '&mrd=0.33864484737666944'
# print(v_url)

hds = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    # 防盗链：溯源上一个页面
    "Referer": url
}

resp = requests.get(v_url, headers=hds)
# print(resp.text)
# print(resp.json().get("videoInfo").get("videos").get("srcUrl"))
# print(resp.json()["videoInfo"]["videos"]["srcUrl"])

video_get_srcUrl = resp.json()["videoInfo"]["videos"]["srcUrl"]
systemTime = resp.json()["systemTime"]

download_url = video_get_srcUrl.replace(systemTime, 'cont-' + videoId)
print(download_url)

with open('video/' + videoId + ".mp4", mode='wb') as f:
    f.write(requests.get(download_url).content)

print('over')
