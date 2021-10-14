# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 20:41
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest
from unittestreport import ddt,list_data
from ddt import data,ddt
from unittest框架.day1.homework.sz_jianghu_44.login import login
from unittest框架.day2.python读取excel操作封装 import read_excel_dict
'''
1、获取测试数据，通过前面封装的read_excel_dict函数读取excel中的内容
2、使用ddt进行参数化，可以使得不同的数据生成不同的测试用例
3、编写测试login的类，准备预期结果
4、调用函数login得到实际结果
5、对预期结果和实际结果进行断言
'''

test_data = read_excel_dict('login_data1.xlsx','Sheet1')

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

        print(type(i['expected']))                  # <class 'str'>
        # 从excel中读取预期结果，数据类型为字符串
        expected = eval(i['expected'])
        actual= login(username,password)
        self.assertEqual(expected,actual)

'''
使用ddt后，第一个用例失败，后面的用例还能够继续执行
总共统计的用例数为3个，第一个失败，后面两个成功
'''




# 使用unittestreport的ddt进行参数化

# 类中声明
@ddt
class Test_Login1(unittest.TestCase):

    # 方法中声明数据
    @list_data(test_data)
    def test_login(self, i):
        # print(i['data'])                # '{"username":"","password":""}'  这是一个字符串
        # 所以使用eval将字符串的的引号去掉，转换成其他数据类型
        # print(i)
        username = eval(i['data'])['username']
        password = eval(i['data'])['password']

        print(type(i['expected']))  # <class 'str'>
        # 从excel中读取预期结果，数据类型为字符串
        expected = eval(i['expected'])
        actual = login(username, password)
        self.assertEqual(expected, actual)