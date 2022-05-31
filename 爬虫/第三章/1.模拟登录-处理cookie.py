# -*- coding: utf-8 -*-
# @Time : 2022/5/25 15:57
# @Author : AMan

import requests

# 会话 -> 一连串的请求，cookie不会丢失
session = requests.session()

# 1.登录
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "13087987456",
    "password": "cx123456"
}
resp = session.post(url=url, data=data)
# print(resp.text)
# <RequestsCookieJar[<Cookie accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F14%252F34%252F91%252F96789134.jpg-88x88%253Fv%253D1653465148000%26id%3D96789134%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BftLNg51aI%26e%3D1669018086%26s%3Da4c7dd0289b9920e for .17k.com/>, <Cookie c_channel=0 for .17k.com/>, <Cookie c_csc=h5 for .17k.com/>, <Cookie uuid=68AECEAE-21EE-47A6-C71C-2D7F810020CF for .17k.com/>]>
# print(resp.cookies)

# 2.拿数据
myBook = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp2 = session.get(myBook)
print(resp2.json())

# {'status': {'code': 10103, 'msg': '用户登陆信息错误'}, 'time': 1653466525000}
# print(requests.get(myBook).json())
