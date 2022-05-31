# -*- coding: utf-8 -*-
# @Time : 2022/5/31 12:24
# @Author : AMan

import time
import pymysql
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# 欢迎来到直播间！抖音严禁未成年人直播或打赏。直播间内严禁出现违法
# msg = web.find_element(by=By.XPATH,
#                        value='//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]')
# s = msg.find_element(by=By.XPATH, value='./div').text
# print(s)

def dy_print_stream_content(web, end_data_id, db, drop_name):
    divs = web.find_elements(by=By.XPATH,
                             value='//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/div')
    for index in range(len(divs)):
        # print("上次的最后一条评论id：", end_data_id)
        d = divs[index]
        try:
            data_id = d.get_attribute("data-id")
            # print('data_id:', data_id)

            if int(end_data_id) == 0:
                # 第一次进入，第一条数据是直播间提示信息，可以直接过滤【欢迎来到直播间！抖音严禁未成年人直播或打赏。直播间内严禁出现违法......】
                print(f"过滤第一条直播间提示信息, 赋值end_data_id：{end_data_id}")
                end_data_id = data_id
                continue
            if int(data_id) <= int(end_data_id):
                # 将重复的数据过滤掉
                # name = d.find_element(by=By.XPATH, value='./div[@class="UPfiLZob"]/span[2]').text
                # content = d.find_element(by=By.XPATH, value='./div[@class="UPfiLZob"]/span[3]').text
                # print(f'输出过了 >>>  {name}:{content}')
                # print(">>> 重复数据...跳过...")
                continue
            name = d.find_element(by=By.XPATH, value='./div[@class="UPfiLZob"]/span[2]').text.replace("：", "")
            content = d.find_element(by=By.XPATH, value='./div[@class="UPfiLZob"]/span[3]').text.replace(":", "")
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            data = {
                "data_id": data_id,
                "name": name,
                "content": content,
                "time_str": time_str,
            }
            insert_db(db, 'test_stream_' + drop_name, data=data)

            print(f'{time_str} {name}:{content}')
            print("------------------")

            end_data_id = data_id
        except:
            print(f">>>>>>>>> 第{index}条异常...跳过...")
            print("------------------------------------")
            continue
    return end_data_id


def insert_db(db, drop_name, data):
    cursor = ''
    try:
        data_id = data["data_id"]
        name = data["name"]
        content = data["content"]
        time_str = data["time_str"]

        cursor = db.cursor()
        sentence = f"insert into {drop_name}(data_id,user_name,say_comment,say_time) values('{data_id}','{name}','{content}','{time_str}')"
        cursor.execute(sentence)
        db.commit()
        cursor.close()
    except pymysql.Error as e:
        print(f'插入数据失败:{data}' + str(e))
    finally:
        cursor.close()


def get_db_connect():
    try:
        db = pymysql.connect(
            user="root",
            password="wo4caoxiang2",
            host="114.132.234.85",
            database="douyin_test",
            port=3306)
        print('数据库连接成功')
        return db
    except pymysql.Error as e:
        print('数据库连接失败' + str(e))
    return None


def test_create_drop(db, drop_name):
    cur = ''
    try:
        drop_name = f'test_stream_{drop_name}'
        cur = db.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {drop_name}')
        sql = f'CREATE TABLE {drop_name}(data_id char(30) ,user_name char(30), say_comment text, say_time datetime)'
        cur.execute(sql)
        print(f'创建表{drop_name}成功')
    except pymysql.Error as e:
        print(f'创建表{drop_name}失败' + str(e))
    finally:
        cur.close()


if __name__ == '__main__':
    # 准备无头浏览器参数
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disbale-gpu")

    web = Chrome(options=opt)
    stream_id = '214498851520'
    web.get(f"https://live.douyin.com/{stream_id}")

    db = get_db_connect()
    drop_name = stream_id + '_' + web.title
    print(drop_name)
    drop_name = drop_name.split('的')[0]
    print(drop_name)
    # 新建表，第一次运行要执行
    test_create_drop(db, drop_name)
    # 测试
    # data = {
    #     "data_id": "7103817866928034846",
    #     "name": "小甜",
    #     "content": "哈哈哈哈虽然很好笑 但是宝贝注意嗓子呀！！！",
    #     "time_str": "2022-05-31 16:41:41",
    # }
    # insert_db(db, 'test_stream_' + drop_name, data=data)

    index = 1
    end_data_id = '0'
    while True:
        end_data_id = dy_print_stream_content(web=web, end_data_id=end_data_id, db=db, drop_name=drop_name)
        print(f"============= 第{index}次获取评论,最后一条：{end_data_id}=============")
        index += 1
        time.sleep(2)
