# -*- coding: utf-8 -*-
# @Time : 2022/5/30 14:24
# @Author : AMan

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web = Chrome()

web.get("http://lagou.com")

# 找到某个元素. 点击它
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[4]/a') # 方法过期
el = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/ul/li[4]/a')
el.click()

time.sleep(1)

# 找到输入框. 输入老师 => 输入回车/点击搜索按钮
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("老师", Keys.ENTER)
web.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys("老师", Keys.ENTER)

time.sleep(1)

div_list = web.find_elements(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div')
for d in div_list:
    name = d.find_element(by=By.XPATH, value='./div[1]/div[1]/div[1]/a').text
    company = d.find_element(by=By.XPATH, value='./div[1]/div[2]/div[1]/a').text
    price = d.find_element(by=By.XPATH, value='./div[1]/div[1]/div[2]/span').text

    print(name, company, price)
