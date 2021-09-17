# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/17 9:56
# @Software       : PythonFullStack
# @Python_verison : 3.7

list = [1,2,4,'jianghu']
j = 100
if j > len(list)-1:
    raise IndexError('索引越界')
print(list[j])

#     raise IndexError('索引越界')
# IndexError: 索引越界