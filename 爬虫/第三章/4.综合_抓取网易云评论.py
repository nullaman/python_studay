# -*- coding: utf-8 -*-
# @Time : 2022/5/25 17:07
# @Author : AMan


import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json

# 网易云代码解析：
aa = """
e0x:
data: "rid=R_SO_4_1500569811&threadId=R_SO_4_1500569811&pageNo=1&pageSize=20&cursor=-1&offset=0&orderType=1"

i0x :
"orderType=1"
csrf_token: ""
cursor: "-1"
offset: "0"
orderType: "1"
pageNo: "1"
pageSize: "20"
rid: "R_SO_4_1500569811"
threadId: "R_SO_4_1500569811"
"""
bb = """
    var bKB4F = window.asrsea(
    a    JSON.stringify(i0x), 
    b    buV3x(["流泪", "强"]), 
    c    buV3x(Rg5l.md), 
    d    buV3x(["爱心", "女孩", "惊恐", "大笑"])
    );
    e0x.data = j0x.cr0x({
        params: bKB4F.encText,
        encSecKey: bKB4F.encSecKey
    })
    
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    
    // 加密   第一次（d，g）dg固定死了，第二次（第一次结果，随机数(已固定)）
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)  //c = 第一次，g转换utf-8，第二次，随机数i的转换
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")// d = 固定字符串
          , e = CryptoJS.enc.Utf8.parse(a) // e = 第一次，d转换， 第二次，第一次加密的结果
          , f = CryptoJS.AES.encrypt( 加密函数，
              e, //e是值第一次是d,第二次是第一次结果，  
              c, // c是密钥：第一次密钥是g，第二次是i
           {  
                iv: d,  // iv是偏移量
                mode: CryptoJS.mode.CBC // 加密模式
            });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    
    e = "010001"
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    g = "0CoJUm6Qyw8W8jud"
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g), // d,g都固定了
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f), // ef固定死了，i固定后，encSecKey就是死的。
        h
    }
    
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e

"""

# 开始代码
song_id = '1500569811'
music_url = 'https://music.163.com/#/song?id=' + song_id
comment_url = 'https://music.163.com/weapi/comment/resource/comments/get'

data = "rid=R_SO_4_1500569811&threadId=R_SO_4_1500569811&pageNo=1&pageSize=20&cursor=-1&offset=0&orderType=1"
d = {
    "rid": "R_SO_4_" + song_id,
    "threadId": "R_SO_4_" + song_id,
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "mwjGh4TsY3UGOOx4"


def get_encSecKey():
    return "768911bcc8bb6d423e259ee9b23e5f25bd24c847183a676ce3d8a5274ca7d2e2f00637c60a0cd59cc433bdc833dcfe6548a4fb16a2a4e194a31f085029730650549af463a6f551a0e37368d1a8cf91df9d116b6f8e12b73cc65c771779fa731cfa7e05388f15da9eda47e4f13bb5c423370d55658d454382f9b41d55ca522b41"


def get_params(data):
    fist = enc_params(data, g)
    second = enc_params(fist, i)
    return second


# 加密需要补齐16的倍数， 例如123456789，差了七个，补齐使用char(7)补齐七个，查了几个补齐几个
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))  # bs64需要转换
    result = str(b64encode(bs), "utf-8")  # 转换成字符串返回
    return result


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}
params = get_params(json.dumps(d))
encSecKey = get_encSecKey()
print(params)
print(encSecKey)
resp = requests.post(comment_url, data={
    "params": params,
    "encSecKey": encSecKey
}, headers=headers)
print(resp)
print(resp.json())

# "mwjGh4TsY3UGOOx4"
# key "768911bcc8bb6d423e259ee9b23e5f25bd24c847183a676ce3d8a5274ca7d2e2f00637c60a0cd59cc433bdc833dcfe6548a4fb16a2a4e194a31f085029730650549af463a6f551a0e37368d1a8cf91df9d116b6f8e12b73cc65c771779fa731cfa7e05388f15da9eda47e4f13bb5c423370d55658d454382f9b41d55ca522b41"
# text "O4HQCU49xflRaQpQXimOTITcwH7VPDMmQRVoHfYvCODLOcpryKQs8diZeXuKIut2WmeE8iR30qpSHrUFv8tG35KVAkMKpyLcE1Ea/pLXPvhFUIayBfsC5qfIxa1SBv65QGLC5ARkfqb0X9Q9ObdRbalTwMyZESFgYdIQq6cOWKELXOcazy1sSg8Uedi/tXAb7rCTqChuFiusfTRxPvHpTCrtTZbzCZt9+eunQkzcC0OsDF9M15Zrncy5D3jtba+qUK0q0jtBcnKkMFF3aXiM4lADfVQfjYi18ncfMXojpDg="
