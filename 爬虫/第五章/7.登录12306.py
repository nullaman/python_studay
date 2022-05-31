# -*- coding: utf-8 -*-
# @Time : 2022/5/30 17:16
# @Author : AMan

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# 如果你的程序被识别到了怎么办?
# 1.chrome的版本号如果小于88 在你启动浏览器的时候(此时没有加载任何网页内容)，向页面嵌入js代码，去掉webdriver
# web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#         unavigator.webdriver = undefined
#         Object.defineProperty(navigator, "webdriver'{
#           get: ()=> undefined})
#         })
#     """
# })
# web.get(url)
# 2.chrome的版本号如果大于等于88
option = Options()
# option.add_experimental_option('exxcludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')
url = "https://kyfw.12306.cn/otn/resources/login.html"
web = Chrome(options=option)
web.get(url)

web.find_element(by=By.XPATH, value='//*[@id="J-userName"]').send_keys("user_1234")
web.find_element(by=By.XPATH, value='//*[@id="J-password"]').send_keys("passworld")
web.find_element(by=By.XPATH, value='//*[@id="J-login"]').click()

time.sleep(3)

btn = web.find_element(by=By.XPATH, value='//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
