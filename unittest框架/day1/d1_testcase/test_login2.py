# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 16:56
# @Software       : PythonFullStack
# @Python_verison : 3.7
import unittest
from python基础.day13.d1_unittest单元测试框架 import test_login


class Login_Test(unittest.TestCase):

    # TestCase
    def test2(self):
        '''
        测试登录函数2
        :return:
        '''
        username = 'jianghu'
        password ='666666'
        expected = {'code': '200', 'msg': '登录成功'}
        actual = test_login(username,password)
        assert expected == actual