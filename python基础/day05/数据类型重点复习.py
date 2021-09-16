# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 9:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、字符串的索引、切片、常用方法
# strip()         # 去空格
# split()         #字符串转换成列表
# join()          # 列表转换成字符串

# 字符串的格式化
# +
# f-string
# format

# 字符串的倒序[::-1]
# 字符串的所有操作都是基于先拷贝一个，然后在新字符串操作

# 2、列表的索引、切片
# 列表的操作增(append,insert,extend)\删(remove,pop,del)\改li[0]='111'\查index,find
# 列表的排序sort、reverse
# 对原列表进行操作

# 3、字典的增删改查通过key
# 字典的key唯一，不重复，不可变，可哈希，重复的话就是用后面一个

# 4、元组的操作
# 不可变、不可以增加、删除、修改
# 查看使用索引
# 单个元组表示方式为
tu1 = (1)
tu = (1,)
print(type(tu1),type(tu))
# <class 'int'> <class 'tuple'>

# 5、集合
# 存储的数据是不可变数据类型
# 集合主要是用来去重

# 6、数据运算
# 算数运算  +,-/,//,%
# 赋值运算    = +=
# 比较运算   <= a <=,==
# 逻辑运算  or not and
# 成员运算 in not in

# 7、数据类型的转换
# int -->str   使用str()
# bool -->str   使用str()
# list -->str   使用join()如果列表元素都是字符串,否则使用str()
# dict -->str   使用str()

li =['1','2','66']
print(''.join(li))
a_list = [1,2,4]
print(type(str(a_list)),a_list)

# str --> int           必须是整形的
# bool --> int
# float --> int
print(int('11'))
print(int(False))
print(int(1.358))


# int  --> bool  非0则为True
# dict  --> bool 非空则为True
# str  --> bool  非空则为True
# float  --> bool 非0则为True
# list  --> bool  非空则为True
# set  --> bool  非空则为True

# 8、list，tuple，dict，set，str区别
#     list，dict为可变数据类型，有序（序列）
#     str，set，tuple为不可变数据类型，无序（散列）
