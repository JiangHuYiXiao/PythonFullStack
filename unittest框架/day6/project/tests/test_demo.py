# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 11:08
# @Software       : PythonFullStack
# @Python_verison : 3.7



# 如果需要使用demo中的数据需要这样导入
# from unittest框架.day6.project.common import demo
#
# print(demo.a)

import sys
print(sys.path)
# ['F:\\PythonFullStack\\unittest框架\\day6\\project\\tests',
# 'F:\\PythonFullStack',
# 'F:\\PythonFullStack\\python基础\\day09\\包和模块',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37',
# 'C:\\Users\\Administrator\\AppData\\Roaming\\Python\\Python37\\site-packages',
# ' C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages',
# 'F:\\PyCharm 2018.2.2\\helpers\\pycharm_matplotlib_backend']


# 直接这样通过项目目录导入是不行的
from common import demo

print(demo.a)           # ModuleNotFoundError: No module named 'project'


# 注意：
# 万一实在导入包或者模块导入不了可以将包设置为Sources root  ******尽量少用，一个项目里面最多设置一个，否则路径也会有很多问题。