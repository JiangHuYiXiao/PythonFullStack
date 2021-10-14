# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 9:24
# @Software       : PythonFullStack
# @Python_verison : 3.7


'''
测试用例函数编写步骤：
1、准备测试数据，也就是函数参数
2、准备预期结果
3、调用被测试函数，得到实际结果
4、使用self.asserEqual等进行断言
'''
import unittest
from unittest框架.day5.AT_Test_Framework.common.read_excel_dict import read_excel_dict
from ddt import ddt,data
from unittest框架.day5.AT_Test_Framework.login import login


test_data = read_excel_dict(r'F:\PythonFullStack\unittest框架\day5\AT_Test_Framework\data\login_data.xlsx','Sheet1')


@ddt
class Test_Login(unittest.TestCase):
    @data(*test_data)
    def test_login1(self,i):
        #准备数据
        username = eval(i['data'])['username']
        password = eval(i['data'])['password']

        # 从excel中读取预期结果，数据类型为字符串
        expected = eval(i['expected'])

        # 调用函数获取实际结果
        actual= login(username,password)
        self.assertEqual(expected,actual)




