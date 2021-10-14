# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 9:29
# @Software       : PythonFullStack
# @Python_verison : 3.7

def login(username=None, password=None):
    if username is None or password is None:
        return {"code": "400", "msg": "用户名或密码为空"}
    if username == 'yuz' and password == '123':
        return {"code": "200", "msg": "登录成功"}
    return {"code": "300", "msg": "用户名或密码错误"}