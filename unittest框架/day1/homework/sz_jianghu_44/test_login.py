# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 17:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest
from unittest框架.day1.homework.sz_jianghu_44.login import login


# 测试类
class Test_Login(unittest.TestCase):
    def test1(self):
        username = 'jianghu'
        password = '2112'
        expected = {"code": "300", "msg": "用户名或密码错误"}
        actual = login(username,password)
        assert expected==actual

    def test2(self):
        username = 'yuz'
        password = '123'
        expected = {"code": "200", "msg": "登录成功"}
        actual = login(username,password)
        assert expected==actual


    def test3(self):
        username = 'yuz'
        password = '123'
        expected = {"code": "2020", "msg": "登录成功"}
        actual = login(username,password)
        assert expected==actual
