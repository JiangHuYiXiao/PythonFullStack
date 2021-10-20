# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/20 15:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 前程贷项目相关接口

    # 1、登录接口
# http://api.lemonban.com:8766/futureloan/member/login

# 登录接口我们可以直接调用，不需要传递token值，但是我们在单独调用其他接口时就需要传递token值
import requests
login_url = 'http://api.lemonban.com:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
data = {"mobile_phone": "13711112222","pwd": "12345678"}
response = requests.post(url=login_url,headers=headers,json=data)

login_response = response.json()
print(login_response)
# {"code":1006,"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved","msg":"请求头X-Lemonban-Media-Type不存在"}
# 表示我们在调用这个接口时必须在请求头中传递X-Lemonban-Media-Type参数和值





    # 2、充值接口
# http://api.lemonban.com:8766/futureloan/member/recharge
# 充值接口调用步骤
# 先调用登录接口，获取token，token_type:Bearer
# 根据接口文档中的的将token值放在指定位置比如请求头，请求体中，一般是在请求头Authorization中，并且在值前面加上前缀Bearer
# 在请求体中传入参数
# 调用接口
token = login_response['data']['token_info']['token']
print(token)
recharge_url = 'http://api.lemonban.com:8766/futureloan/member/recharge'
headers = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization":f"Bearer {token}"}
data = {"mobile_phone": "13711112222","pwd": "12345678","member_id":10003494,"amount":10000}
recharge_response= requests.post(url=recharge_url,headers=headers,json=data)
print(recharge_response.json())

# {'code': 0, 'msg': 'OK',
#  'data': {'id': 10003494, 'leave_amount': 685422.0, 'mobile_phone': '13711112222', 'reg_name': 'peter',
#           'reg_time': '2021-07-18 10:06:48.0', 'type': 1},
#  'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
