# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 9:05
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 像我们之前的项目都有很多路径相关的比如用例文件的路径，日志文件路径，我们可以通过Python中的os模块进行读取
# 这种操作方式就是动态路径

import os

# 1、当前文件所在绝对路径
cunrrent_file = os.path.abspath(__file__)           # __file__表示当前文件的名称
print(cunrrent_file)            # F:\PythonFullStack\unittest框架\day6\动态路径.py


# 2、获取某个文件的目录
file_dir = os.path.dirname(cunrrent_file)
print(file_dir)         # F:\PythonFullStack\unittest框架\day6


# 3、路径拼接
join_file= os.path.join(file_dir,'动态路径.py')
print(join_file)            # F:\PythonFullStack\unittest框架\day6\动态路径.py