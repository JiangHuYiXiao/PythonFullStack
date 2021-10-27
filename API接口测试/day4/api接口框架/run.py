# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/22 10:32
# @Software       : PythonFullStack
# @Python_verison : 3.7

import unittest,unittestreport
from datetime import datetime

now_time = datetime.now()
time_fmt = now_time.strftime('%Y-%m-%d-%H-%M-%S')
# print(time_fmt)

# 收集用例
# cases是用例所在目录
suite = unittest.defaultTestLoader.discover('cases')            #

# 运行用例
runner = unittestreport.TestRunner(suite=suite,filename=f'auto-test-report-{time_fmt}',templates=1,tester='jianghu',report_dir="./reports")
runner.run()