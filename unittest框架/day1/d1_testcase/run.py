# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/27 16:57
# @Software       : PythonFullStack
# @Python_verison : 3.7
import unittest
import unittest,HTMLTestRunner,HTMLTestRunner_cn,HTMLTestRunner_PY3
import unittestreport
# 收集用例
suite = unittest.defaultTestLoader.discover('./')

# 运行用例
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 测试报告
# 有unittest默认的三种测试报告：HTMLTestRunner,HTMLTestRunner_cn,HTMLTestRunner_PY3
    # file = open('./result.html',mode='wb')
    # HTMLTestRunner
    # runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')

    # HTMLTestRunner_cn
    # file = open('./result1.html',mode='wb')
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')
    # HTMLTestRunner_PY3
    # file = open('./result.html',mode='wb')
    # runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')
    #
    # runner.run(suite)


# 也可以用一些第三方的开源的测试报告比如unittestreport
# pip install unittestreport

runner = unittestreport.TestRunner(suite,filename='登录测试报告',tester='jianghu',templates=1)
runner.run()