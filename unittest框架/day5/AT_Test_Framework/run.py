# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 9:21
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest,unittestreport

# 收集用例
# cases是用例所在目录
suite = unittest.defaultTestLoader.discover('cases')            #

# 运行用例
runner = unittestreport.TestRunner(suite=suite,filename='自动化测试报告',templates=1,tester='jianghu',report_dir="./reports")
runner.run()

