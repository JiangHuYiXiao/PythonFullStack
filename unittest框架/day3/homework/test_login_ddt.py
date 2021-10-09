# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 18:48
# @Software       : PythonFullStack
# @Python_verison : 3.7


import unittest
from unittestreport import ddt,list_data
from ddt import data,ddt
from unittest框架.day1.homework.sz_jianghu_44.login import login
from unittest框架.day3.homework.read_excel_dict import read_excel_dict


test_data = read_excel_dict('login_data.xlsx','Sheet1')

# 使用unittest自带的ddt进行参数化
# 类中声明
@ddt
class Test_Login(unittest.TestCase):

    # 方法中声明数据
    @data(*test_data)     # 需要进行解包操作
    def test_login(self,i):
        # print(i['data'])                # '{"username":"","password":""}'  这是一个字符串
        # 所以使用eval将字符串的的引号去掉，转换成其他数据类型
        # print(i)
        username = eval(i['data'])['username']
        password = eval(i['data'])['password']

        # print(type(i['expected']))                  # <class 'str'>
        # 从excel中读取预期结果，数据类型为字符串
        expected = eval(i['expected'])
        actual= login(username,password)
        self.assertEqual(expected,actual)
