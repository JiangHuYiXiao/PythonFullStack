# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 20:41
# @Software       : PythonFullStack
# @Python_verison : 3.7


'''
对我们之前写的一个login函数进行测试

测试步骤为：
1、根据被测试函数的参数，准备测试数据
2、准备预期结果
3、调用被测函数login，得到实际结果
4、对预期结果和实际结果进行断言，判断用例是否通过
'''

import unittest
# from unittest框架.day1.homework.sz_jianghu_44 import login
from unittest框架.day1.homework.sz_jianghu_44.login import login
class Test_Login(unittest.TestCase):
    def test_login_null(self):
        '''
        对登录函数进行测试，场景为用户名和密码为空
        :return:
        '''
        username = None
        password = None
        expected = {"code": "400", "msg": "用户名或密码为空"}
        actual= login(username,password)
        self.assertEqual(expected,actual)

    def test_login_error(self):
        '''
        对登录函数进行测试，场景为用户名和密码为空
        :return:
        '''
        username = 1
        password = 2
        expected = {'code': '300', 'msg': '用户名或密码错误'}
        actual= login(username,password)
        self.assertEqual(expected,actual)


    def test_login_successful(self):
        '''
        对登录函数进行测试，场景为用户名和密码为空
        :return:
        '''
        username = 'yuz'
        password = '123'
        expected = {'code': '200', 'msg': '登录成功'}
        actual= login(username,password)
        self.assertEqual(expected,actual)


'''
但是这样编写测试用例时的代码，重复性太高了，
且用例数据修改需要修改代码，比较繁琐，所以我们一般需要对用例数据和代码进行分开，使用excel、yaml对用例数据进行管理，这样就可以做到测试数据分离。
下一步我们继续优化
'''