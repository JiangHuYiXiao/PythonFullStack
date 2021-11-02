# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/1 10:55
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、jsonpath的作用主要是用来获取多个json层级数据的，不至于去写多个嵌套进行获取值

# 2、安装jsonpath

# 3、导入jsonpath
from jsonpath import jsonpath

login_response = {'code': 0, 'msg': 'OK',
                  'data': {'id': 1237001403, 'leave_amount': 203575.7, 'mobile_phone': '15100002222', 'reg_name': '小柠檬',
                           'reg_time': '2021-10-23 21:40:13.0', 'type': 1,
                           'token_info': {'token_type': 'Bearer', 'expires_in': '2021-11-01 11:07:51',
                                          'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEyMzcwMDE0MDMsImV4cCI6MTYzNTczNjA3MX0.hKMtFrrHpFJpdCD0VejrgaXqI9zoOK2azndvGq17jElEgYpJIs_JQdmsmraxmMwIBPptpMBf9jOBIXfi7FvlRg'}},
                  'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}

# jsonpath()返回的是一个元组，所以需要再使用索引进行获取值
# .表示儿子层级
# ..表示子孙后代所有的层级
# 以后我们全部都用$..变量名就可以获取任何层级的数据了
member_id = jsonpath(login_response,'$..id')
login_token = jsonpath(login_response,'$..token')
print(member_id)
print(login_token)