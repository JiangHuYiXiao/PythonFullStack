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
from unittest框架.day5.AT_Test_Framework.common.AT_logger import at_logger
from unittest框架.day5.AT_Test_Framework.common.AT_logger import my_log

test_data = read_excel_dict(r'F:\PythonFullStack\unittest框架\day5\AT_Test_Framework\data\login_data.xlsx','Sheet1')


@ddt
class Test_Login(unittest.TestCase):
    @data(*test_data)
    def test_login1(self,i):
        # 记录日志
        # at_logger('jianghu.log').info('正在执行测试用例')      # 这样写我们的logger是没有关闭的，因为有三组数据，记录日志是呈现1,2,3加起来的6个日志记录的
        my_log.info('正在执行测试用例')


        #准备数据
        username = eval(i['data'])['username']
        password = eval(i['data'])['password']

        # 从excel中读取预期结果，数据类型为字符串
        expected = eval(i['expected'])

        # 调用函数获取实际结果
        actual= login(username,password)
        self.assertEqual(expected,actual)




