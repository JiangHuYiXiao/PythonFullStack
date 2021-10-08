# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 18:24
# @Software       : PythonFullStack
# @Python_verison : 3.7

# fixture：测试固件，就是一个测试用例运行的一个前置条件、后置处理。
# 一般有setUp，tearDown，每个用例之前和之后都会自动执行一次
# setUpClass，tearDownClass  整个测试类只会执行一次

import unittest
class Test_database(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('每个测试类开始只执行一次')

    @classmethod
    def tearDownClass(cls):
        print('每个测试类结束只执行一次')

    def setUp(self):
        print('链接数据库')

    def tearDown(self):
        print('断开数据库')

    def test_data1(self):
        print('正在执行测试数据1')
        self.assertEqual(1,1,'实际结果和预期结果不相等')

    def test_data2(self):
        print('正在执行测试数据2')
        self.assertEqual(1,2,'实际结果和预期结果不相等')

