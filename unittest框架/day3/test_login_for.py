# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 20:41
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest
# from unittest框架.day1.homework.homework import login
from unittest框架.day1.homework.sz_jianghu_44.login import login
from unittest框架.day2.python读取excel操作封装 import read_excel_dict
'''
1、获取测试数据，通过前面封装的read_excel_dict函数读取excel中的内容
2、编写测试login的类，准备预期结果
3、调用函数login得到实际结果
4、对预期结果和实际结果进行断言
'''

data = read_excel_dict('login_data1.xlsx','Sheet1')
class Test_Login(unittest.TestCase):

    def test_login_null(self):

        '''
        对登录函数进行测试，场景为用户名和密码为空
        :return:
        '''
        for i in data:
            # print(i['data'])                # '{"username":"","password":""}'  这是一个字符串
            # 所以使用eval将字符串的的引号去掉，转换成其他数据类型
            username = eval(i['data'])['username']
            password = eval(i['data'])['password']
            expected = {"code": "400", "msg": "用户名或密码为空"}
            actual= login(username,password)
            self.assertEqual(expected,actual)


'''
使用for循环会报错：
存在两个问题：
1、统计用例条数只有一个，我们实际却是有三个用例数据
因为第一个用例失败了，后面的用例都不会执行了
2、username = i['data']['username']
TypeError: string indices must be integers
类型错误，因为excel中没有字典这个数据类型，excel读取出来的数据都是字符串,可以通过eval()进行去引号
后续我们需要继续优化解决只有一个用例的问题，这样就可以有多少数据就有多少用例
就需要用到参数化，也就是数据驱动ddt
参数化：对统一的逻辑使用不同的数据（参数）去执行
'''
