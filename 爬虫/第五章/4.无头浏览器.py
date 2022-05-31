# -*- coding: utf-8 -*-
# @Time : 2022/5/30 15:57
# @Author : AMan

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# 浏览器配置 可以看3
from selenium.webdriver.chrome.options import Options
# 下拉框选择等操作
from selenium.webdriver.support.select import Select

# 准备无头浏览器参数
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)

web.get("https://www.endata.com.cn/Box0ffice/B0/Year/index.html")

# 定位到下拉列表
sel_el = web.find_element(by=By.XPATH, value='//*[@id="OptionDate"]')  # 对元素进行包装，包装成下拉菜单 sel =Select(selel)# 让浏览器进行调整选项
sel = Select(sel_el)

for i in range(len(sel.options)):  # i就是每一个下拉框选项的索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    time.sleep(2)
    table = web.find_element(by=By.XPATH, value='//*[@id="TableList"]/table')
    print(table.text)  # 打印所有文本信息 print("imiiii

print("运行完毕。")
web.close()

# 获取页面源代码
# print(web.page_source)
