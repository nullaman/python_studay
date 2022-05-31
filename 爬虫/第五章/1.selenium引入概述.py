# -*- coding: utf-8 -*-
# @Time : 2022/5/30 11:30
# @Author : AMan

# 能不能让我的程序连接到浏览器 ，让浏览器来完成各种复杂的操作，我们只接受最终的结果
# selenium:自动化测试工具
# 可以:打开浏览器。然后像人一样去操作浏览器
# 程序员可以从selenium中直接提取网页上的各种信息
# 环境搭建:
#   pip install selenium -i 清华源
#   下载浏览器驱动:https://npmmirror.com/package/chromedriver
#   https://sites.google.com/chromium.org/driver/?spm=a2c6h.24755359.0.0.23a552e5iN2BgO
#       把解压缩的浏览器驱动 chromedriver 放在python解释器所在的文件夹

# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome

# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网站
# web.get("www.baidu.com") # 报错
web.get("https://www.baidu.com/")

print(web.title)