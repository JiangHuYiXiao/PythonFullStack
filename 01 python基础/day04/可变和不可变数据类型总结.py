# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 18:42
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 可变数据类型[list,dict]

# 不可变数据类型[str,int,tuple]

# 可变和不可变指的是元素是否可以修改
a1 = [1,2,('a','b')]

# 修改列表中的元素
a1[1] = 100
print(a1)               # [1, 100, ('a', 'b')]

# a1[2] = 'hello'
# print(a1)           # [1, 100, 'hello']

# 修改元组中的元素
a1[2][0] = 'A'          # TypeError: 'tuple' object does not support item assignment  元组不可变
print(a1)


a2 = (1,2,['a','b'])
# 修改元组中包含的列表元素
a2[2][0] = 'hello'
print(a2)

# 修改元组的元素
a2[2] = 'hhhh'          # TypeError: 'tuple' object does not support item assignment