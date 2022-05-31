# -*- coding: utf-8 -*-
# @Time : 2022/5/30 16:54
# @Author : AMan

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.get("https://www.chaojiying.com/user/login/")

# 图片验证码区域 暂存为图片
png = web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# 超级鹰识别图片
cjy = Chaojiying_Client('cx452487506', 'cx123456', '934350')
dic = cjy.PostPic(png, 1902)
print(dic)
pic_str = dic["pic_str"]
print(pic_str)

web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("cx452487506")
web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("cx123456")
web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(pic_str)
time.sleep(3)

web.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
# time.sleep(100)
# 不关闭浏览器 【没有用】
# ActionChains(web).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# time.sleep(100)
