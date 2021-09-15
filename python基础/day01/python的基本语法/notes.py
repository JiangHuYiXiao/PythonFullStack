# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/9 10:14
# @Software       : PythonFullStack
# @Python_verison : 3.7

# python基本语法：
# 变量:
#     定义：a = 2
#     作用：存储数据
#     命名规则：
#         字母、数字、下划线组成
#         不能是数字开头
#         不能是python预置的关键字
#         # 尽量做到变量名，见名知意
#
# 数据类型：
#     int   整数 2
#     float     浮点数 2.36
#     str   字符串 用单引号或者双引号，或者是三引号包含内容
#     bool  布尔 False， True
#     list  列表 [1,2,'4',a]
#     dict  字典 {'a':1,'b':'bb'}
#     tuple 元组 (1,2,3)
#     set  集合 {a,b,c}   空集合使用set() 因为空字典为{}
#     None类型  是一个特殊的数据类型

# 查看数据类型type()
# print(type(2))
# print(type('2'))
print(None)      # None

# 数据类型转换
# 1、其他数据类型转换成str，基本上所有的数据类型都可以转换成str
# int --> str
# print(str(12),type(str(12)))     # <class 'str'>
#
# float -->str
# print(str(1.2334),type(str(1.2334)))   # <class 'str'>
#
# bool -->str
# print(str(False),type(str(False)))   # False <class 'str'>
#
# list -->str
# print(str([1, 2, 3]),type(str([1, 2, 3])))  # [1, 2, 3] <class 'str'>