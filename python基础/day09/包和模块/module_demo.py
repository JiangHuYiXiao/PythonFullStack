# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/15 14:52
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 模块：所有的.py文件就可以称为模块，
# 包：package，包含__init__.py文件，都可以称为包


# 1、包和模块的导入
# 因为导入一个模块时会先从sys.modules下面查看是否存在这个模块，存在就不再导入是根据sys.path,去导入的
import sys
print(sys.path)

# ['F:\\PythonFullStack\\python基础\\day09\\包和模块',
#  'F:\\PythonFullStack',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37',
#  'C:\\Users\\Administrator\\AppData\\Roaming\\Python\\Python37\\site-packages',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages',
#  'F:\\PyCharm 2018.2.2\\helpers\\pycharm_matplotlib_backend']

# 2、
# from python基础.day05 import func.py




