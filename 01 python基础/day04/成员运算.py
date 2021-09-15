# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 17:10
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 成员运算：指的某个成员是否在符合的数据类型中（tuple，str，list，dict，set），可以理解为是否是其子集，返回值为bool类型
# 关键字为in，not in


# list
list = [1,'q','b',11]
print(1 in list)            # True
print(111 in list)          # False
print(111 not in list)          # True

# str
str = 'jianghuyixiao'
print('i' in str)           # True
print('ii' in str)          # False
print('ii' not in str)          # True




# 字典的存储是key和value是分开存储的，只能通过key的内存地址找value，所以对字典进行成员运算，判断的是key

# dict
dict = {'name':'江西','address':'武功山'}
print('name' in dict)           # True
print('江西' in dict)             # False


# set
set = {1,2,'hhh','ooo'}
print('hhh' in set)         # True
print('hhh' not in set)         # False