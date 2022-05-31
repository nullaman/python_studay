# -*- coding: utf-8 -*-
# @Time : 2022/5/30 15:09
# @Author : AMan


import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 准备无头浏览器参数
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)

web.get("http://lagou.com")

# 找到某个元素. 点击它
web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/ul/li[4]/a').click()

time.sleep(3)

# 找到输入框. 输入老师 => 输入回车/点击搜索按钮
web.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys("老师", Keys.ENTER)

time.sleep(3)

div_list = web.find_elements(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div')
index = 1
for d in div_list:
    name = d.find_element(by=By.XPATH, value='./div[1]/div[1]/div[1]/a').text
    company = d.find_element(by=By.XPATH, value='./div[1]/div[2]/div[1]/a').text
    price = d.find_element(by=By.XPATH, value='./div[1]/div[1]/div[2]/span').text
    print(name, company, price)
    time.sleep(3)

    # 点击职位
    d.find_element(by=By.XPATH, value='./div[1]/div[1]/div[1]/a').click()
    # 切换窗口
    web.switch_to.window(web.window_handles[-1])
    time.sleep(3)
    # 获取职位的文本输出
    content = web.find_element(by=By.XPATH, value='//*[@id="job_detail"]/dd[2]/div').text
    print(content)
    web.close()
    web.switch_to.window(web.window_handles[0])
    print(f"---------------完成 {index} 个---------------------")
    index += 1
    time.sleep(3)

iframe = web.find_element("")
web.switch_to.frame(iframe)
web.switch_to.default_content()  # 切换回原页面
