# -*- coding: utf-8 -*-
# @Time : 2022/5/23 14:29
# @Author : AMan
import time

import schedule


def job():
    print("hahahaha")


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
