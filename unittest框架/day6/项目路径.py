# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 9:05
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、项目路径
# 首先我们如果要在pycharm中打开某个项目，必须通过file下的open直接打开这个项目，而不要打开这个项目的上层目录后再打开项目。

# 2、比如我现在的项目是project，然后我用pycharm直接打开project这个项目，那么project所在的路径就是项目路径
# 然后我要在test_demo.py中导入common中的demo那么我们可以这样导入：
# from common import demo


# 3、如果像我现在打开的项目是PythonFullStack那么我要在test._demo.py中导入demo是这样导入的
# from unittest框架.day6.project.common import demo


# ***********************所有的导包、模块都是从项目路径的根目录的儿子层开始导入****************************

# 所谓项目路径就是在pycharm打开的项目就是项目路径，然后导包就要从该目录开始导入

