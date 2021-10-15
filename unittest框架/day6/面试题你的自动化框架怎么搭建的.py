# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/14 20:04
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 你的自动化测试框架怎么搭建？，或者你们公司自动化框架包含什么目录？
# 1、使用分层设计，不同的内容放在不同的包中或者模块中，分层次，便于后续维护
# 2、详细描述每个包、模块的作用
    # 测试用例cases包
    # 测试数据data包
    # 测试报告report包
    # 通用功能 common包包含excel数据读取，yaml数据读取
    # 配置文件config包
    # 运行文件run.py


# 3、解决了哪些接口自动化的问题
    # 数据驱动
    # 数据库断言
    # 数据提取
    # 动态参数获取
