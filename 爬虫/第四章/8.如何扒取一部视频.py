# -*- coding: utf-8 -*-
# @Time : 2022/5/27 12:55
# @Author : AMan


# <video src="不能播的视频.mp4"></video># 一般的视频网站是怎么做的?
# 用户上传 -> 转码(把视频做处理，2K，1080，标清) 切片处理(把单个的文件进行拆分) 60
# 用户在进行拉动进度条的时候
#

# 需要一个文件记录:1.视频播放顺序，2.视频存放的路径。
# M3U8 txt json =>文本
# 想要抓取一个视频:
# 1.找到m3u8(各种手段)# 2，通过m3u8下载到ts文件
# 3，可以通过各种手段(不仅是编程手段)把ts文件合并为一个mp4文件


# 合并视频
# mac: cat 1.ts 2.ts 3.ts > xxx.mp4
# windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
# import os
# os.system(f"cat {str} > movie.mp4")
# os.system(f"copy /b {str} movie.mp4")
