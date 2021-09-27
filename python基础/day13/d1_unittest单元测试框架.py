# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 15:53
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、单元测试
# 对代码中的最小单元进行测试，一般是指的函数、或者类中的方法

# 在没有使用单元测试框架unittest时我们也可以进行单元测试
    # 1、写一个测试函数，手工调用测试函数
    # 2、使用assert进行断言判断当测试用例失败后，加上异常处理
    # 3、收集测试用例
    # 4、运行测试用例

# 但是这样测试比较麻烦，所以才有专门的单元测试框架，框架中包含已经封装好的功能提供给我们使用。


# 2、单元测试框架
    # unitetest是python内置的单元测试框架，免安装
    # pytest是一个第三方的单元测试框架，需要安装pip或者编译器上安装



# 3、unittest框架使用
# 使用unittest框架时，测试的类必须继承TestCase类
# 测试用例（方法）名称必须是以test开头test*
# 当我们运行unittest文件时，会自动帮我们收集用例
# 会自动帮我们运行用例

# 4、unittest几个常用的概念
# TestCase：测试用例，一般我们把所有的测试用例放到一个文件夹中
# TestSuite ： 测试套件，也就是测试用例集合,使用suite = unittest.defaultTestLoader.discover('./')收集用例
# TextTestRunner： 运行测试用例  runner = unittest.TextTestRunner()     runner.run(suite)

import unittest

# 被测函数
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

