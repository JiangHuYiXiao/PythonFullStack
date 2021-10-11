# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/11 10:37
# @Software       : PythonFullStack
# @Python_verison : 3.7


'''
日志定义：就是程序运行时的信息，可以直接打印，也可以记录到文件中。
作用：记录程序运行时的信息后，如果出错了，后面可以通过日志进行问题解决。

日志级别：
NOSET    无
debug       调试信息
info   正常信息，用于记录步骤
warning  警告
error    错误，用于记录错误
critical  严重

python记录日志的库，有loguru，logging


日志输出到窗口


日志最重要的是写入文件，供后续查看
'''

from loguru import logger
import unittest
from unittest框架.day1.homework.sz_jianghu_44.login import login
# logger.info('这是程序运行的正常日志信息')
# logger.error('这是程序报错时候的日志信息')

# 2021-10-11 10:58:56.381 | INFO     | __main__:<module>:25 - 这是程序运行的正常日志信息
# 2021-10-11 10:58:56.381 | ERROR    | __main__:<module>:26 - 这是程序报错时候的日志信息

logger.add(sink='run.log',encoding='utf-8',rotation='1KB',level='ERROR')
# rotation表示文件最多能够存储的大小,超过这个大小则会新建问题件level,表示记录额日志级别
# rotation还可以支持每一段时间新建一个文件
class Test_Login(unittest.TestCase):
    def test_login1(self):

        # info级别的日志我们可以写在任何位置
        logger.info('用例1在执行')
        username = 'jianghu'
        password = '2112'
        expected = {"code": "3010", "msg": "用户名或密码错误"}
        actual = login(username,password)
        try:
            self.assertEqual(expected,actual)
        except AssertionError as e:
            # error日志一般放在会出错的代码之后
            logger.error('用例1断言失败')
            # 捕获了异常后，必须抛出，否则不会记录到错误信息
            raise e

        # 主动抛出异常后，后面的代码也不会继续执行了
        print('****************************************')

    def test_login2(self):
        logger.info('用例2在执行')
        username = 'jianghu'
        password = '2112'
        expected = {"code": "300", "msg": "用户名或密码错误"}
        actual = login(username,password)
        self.assertEqual(expected, actual)

# 2021-10-11 11:18:35.355 | INFO     | 日志模块loguru:test_login1:38 - 用例1在执行
# 2021-10-11 11:18:35.355 | ERROR    | 日志模块loguru:test_login1:47 - 用例1断言失败
# 2021-10-11 11:18:35.361 | INFO     | 日志模块loguru:test_login2:52 - 用例2在执行