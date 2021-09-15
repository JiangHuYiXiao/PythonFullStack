# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 17:10
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、集合的定义：
set1 = {1,2,3}
print(type(set1))           # <class 'set'>

# 2、集合的作用：存储数据，存储的数据是不可重复的,会自动去重复
set1 = {1,2,3,1,2,3,4,58,2}
print(set1)         # {1, 2, 3, 4, 58}
# 3、空集合
null_set = set()
print(type(null_set))       # <class 'set'>

# 3、集合的数据类型必须是不可变数据类型,也就是可以哈希的数据

set2 = {1,2,[12,22]}
print(set2)         # TypeError: unhashable type: 'list'