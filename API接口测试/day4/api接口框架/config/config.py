# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 9:20
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 使用动态路径
import os

# 当前文件绝对路径
current_file = os.path.abspath(__file__)


# 配置文件的目录路径
config_dir = os.path.dirname(current_file)

# 项目的根目录AT_Test_Framwork
root_dir = os.path.dirname(config_dir)
# print(root_dir)      # F:\PythonFullStack\unittest框架\day5\AT_Test_Framework


# 测试数据目录路径

data_dir = os.path.join(root_dir,'data')

# 测试数据路径
testdata_file = os.path.join(data_dir,'cases_data.xlsx')
# print(testdata_file)


# 测试日志目录

log_dir = os.path.join(root_dir,'reports')

# 测试日志文件路径
log_file = os.path.join(log_dir,'AT_test.log')

host = 'http://api.lemonban.com:8766/futureloan'