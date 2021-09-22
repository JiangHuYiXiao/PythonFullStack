# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/15 14:52
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 模块：所有的.py文件，就可以称为模块。
# 包：package，包含__init__.py文件夹，都可以称为包。


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

# 2、from 包名 import 模块名
# 包名是需要先看下有哪些路径添加到了sys.path下，然后再已经有的路径基础下进行导入
# 'F:\\PythonFullStack',所以从这个路径下开始导入，也可以从项目根目录开始导入

from python基础.day05 import func
print(func.test())



# 3、from 包名.模块名 import 函数名、类名、变量
# 、方法名是不能够直接导入的，需要先导入类，然后通过类去使用方法

# 导入函数
from python基础.day05.func import test
print(test())


# from python基础.day05.func import small_student
# from python基础.day05.func.Student import small_student
# ImportError: cannot import name 'small_student from 'python基础.day05.func' (F:\PythonFullStack\python基础\day05\func.py)

# 导入类
from python基础.day05.func import Student

print(Student)

Student.small_student()             # 这样才可以使用方法
# 导入变量
from python基础.day05.func import time1
print(time1)




# 当本文件有相同的变量、函数、类、方法时，使用别名进行导入
def test():
    return 'hhhhh'
from python基础.day05.func import test as test_one
print(test())               # hhhhh
print(test_one())


# 如果导入的文件和sys.path中路径一样，则不需要from
import func2

print(func2.f())







