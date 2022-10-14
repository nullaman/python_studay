# -*- coding: utf-8 -*-
# @Time : 2021/10/19 9:44
# @Author : AMan

import pyautogui
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler  # 阻塞当前进程的调度器

# blocking类型调度器会阻塞当前进程，若你想要后台运行的调度器，可以使用以下代码：
# from apscheduler.schedulers.background import BackgroundScheduler

pyautogui.PAUSE = 1  # 设置每一步操作的间隔（秒），可防止操作太快

# icon_position = pyautogui.position()
# print(icon_position) # 打印坐标，Point(x=1568, y=1061)
# entry_position = pyautogui.position()
# print(entry_position) # 打印坐标，Point(x=899, y=822)

# pyautogui.click(x=1568, y=1061) # 默认左键单击
# pyautogui.click(x=899, y=822)
# pyautogui.hotkey('ctrl', 'alt', 'w') # 按下组合键的方法，ctrl+v粘贴

pyautogui.moveTo(x=1568, y=1061, duration=2)  # duration为执行时长，可选
pyautogui.click(x=1568, y=1061)
pyautogui.moveTo(x=899, y=822, duration=2)
pyautogui.click(x=899, y=822)
# 第二个参数为按下每一个字母的间隔，可选
pyautogui.typewrite([*list('zhengzai '), *list('jinxing '), 'shift', *list('pyautogui'), 'shift', *list('shiyan ')
                        , 'enter'], 0.1)
