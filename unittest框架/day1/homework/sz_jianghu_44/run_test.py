# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 17:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest,unittestreport

# 收集测试用例
suite = unittest.defaultTestLoader.discover('./')

# 运行测试用例
runner = unittestreport.TestRunner(suite,filename='登录测试报告',tester='jianghu',templates=1)
runner.run()
