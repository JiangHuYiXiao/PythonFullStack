# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/19 19:59
# @Software       : PythonFullStack
# @Python_verison : 3.7

'''

根据上课内容，完成前程贷项目的充值处理。

先登录获取 token, 再访问充值接口，接口需要携带请求头

{"X-Lemonban-Media-Type": "lemonban.v2"}


测试账号：
"mobile_phone": "13711112222",
"pwd":"12345678"


登录接口：http://api.lemonban.com:8766/futureloan/member/login
充值接口：http://api.lemonban.com:8766/futureloan/member/recharge

'''
# 登录接口调用得到token，token_type
import requests
login_url = 'http://api.lemonban.com:8766/futureloan/member/login'
# 在请求头中添加参数
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
# 在请求体中添加参数
data = {"mobile_phone": "13711112222","pwd": "12345678"}
response = requests.post(url=login_url,headers=headers,json=data)
# 使用json格式方便后面取token值
login_response = response.json()
print(login_response)


# 充值接口调用步骤
# 先调用登录接口，获取token，token_type:Bearer
# 根据接口文档中的的将token值放在指定位置比如请求头，请求体中，一般是在请求头Authorization中，并且在值前面加上前缀Bearer
# 在请求体中传入参数
# 调用接口

# token值
token = login_response['data']['token_info']['token']
# print(token)
recharge_url = 'http://api.lemonban.com:8766/futureloan/member/recharge'
headers = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization":f"Bearer {token}"}
data = {"mobile_phone": "13711112222","pwd": "12345678","member_id":10003494,"amount":10000}
recharge_response= requests.post(url=recharge_url,headers=headers,json=data)
print(recharge_response.json())