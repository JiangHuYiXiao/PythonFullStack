# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 16:56
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest
def test_login(username=None,password=None):
    if username is None or password is None:
        return{'code':'201','msg':'用户名或者密码不能为空'}
    if username == 'jianghu' and password =='666666':
        return {'code': '200', 'msg': '登录成功'}
    return {'code': '202', 'msg': '用户名或者密码错误'}


# 测试类
class Login_Test(unittest.TestCase):

    # TestCase
    def test1(self):
        '''
        测试登录函数1
        :return:
        '''
        username = 'hhh'
        password ='122'
        expected = {'code': '203', 'msg': '用户名或者密码错误'}
        actual = test_login(username,password)
        assert expected == actual


