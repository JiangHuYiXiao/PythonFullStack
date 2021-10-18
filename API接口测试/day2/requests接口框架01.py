# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/18 8:43
# @Software       : PythonFullStack
# @Python_verison : 3.7

# python中接口测试框架为requests
import requests

res = requests.get('https://www.baidu.com/')
print(res)    # 返回一个对象<Response [200]>

print(res.text)             #  返回一个字符串的数据类型，存储网页信息
print(res.content)             # 返回一个byte数据类型，存储网页信息
print(res.json())               # 返回一个字典的数据类型，存储的网页信息
print(res.status_code)              # 200


