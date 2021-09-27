# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:06
# @Software       : PythonFullStack
# @Python_verison : 3.7

# login(username=None, password=None):
# if username is None or password is None:
# return {"code": "400", "msg": "用户名或密码为空"}
# if username == 'yuz' and password == '123':
# return {"code": "200", "msg": "登录成功"}
# return {"code": "300", "msg": "用户名或密码错误"}def
#
# 1，使用 unittest 对上面的函数进行测试
# 2, 在 login.py 文件中保存上面的函数
# 3，在 test_login.py 文件中编写测试用例函数，根据需求设计多个用例函数。
# 4，在 run_test.py 文件中收集用例，并使用 unittestreport 完成测试报告生成。

import unittest

# 被测试函数
def login(username=None, password=None):
    if username is None or password is None:
        return {"code": "400", "msg": "用户名或密码为空"}
    if username == 'yuz' and password == '123':
        return {"code": "200", "msg": "登录成功"}
    return {"code": "300", "msg": "用户名或密码错误"}



