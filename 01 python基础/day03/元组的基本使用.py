# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 8:55
# @Software       : PythonFullStack
# @Python_verison : 3.7
# 1、元组定义
tup = ()            # 表示一个空元组

# 2、元组的作用，存储不可变类型的数据


# 3、一个元素的元素需要在元素后加逗号，不加的话则还是原来的数据类型
tup1 = ('aa')
tup2 = ('aa',)
print(type(tup2))           # <class 'tuple'>
print(type(tup1))           # <class 'str'>

# 4、元组不可以增加、删除、修改
# tup2.pop()      # AttributeError: 'tuple' object has no attribute 'pop'

# 5、元组的查看
tuple = (1,2,5,'abc','123')
print(tuple[0])         # 1
print(tuple[4])         # 123

print(tuple.index('abc'))           # 3