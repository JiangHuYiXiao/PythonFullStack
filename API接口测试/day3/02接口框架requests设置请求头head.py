# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/20 8:59
# @Software       : PythonFullStack
# @Python_verison : 3.7

import requests
url = 'http://httpbin.org/get'
response = requests.request(method='GET',url=url)
print(response.text)




# 设置请求头，默认首字母会大写

# 添加参数
headers ={"name":"jianghu","age":"11"}
response = requests.request(method='GET',url=url,headers=headers)
print(response.text)

# 修改参数
# "User-Agent": "python-requests/2.24.0",
headers = {"User-Agent":"chrome"}
response = requests.request(method='GET',url=url,headers=headers)
print(response.text)