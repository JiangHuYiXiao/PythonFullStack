# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 16:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、**********字典的定义：****************
dict = {'key1':1,'key2':2}

# 2、***********字典的作用*****************
# 存储数据，以键值对的方式存储，用key表示具体意义，value表示值。
# 之前的列表虽然也可以存储数据，但是无法标记每个数据的具体意义，所以就有了字典数据类型。
# 字典无序

# 3、**********在一个字典中key的注意点************
# key不可以重复，唯一的，如果重复则前面的key:value会丢失
# key的数据类型一般是字符串，但是也可以是其他数据类型，如果我们为了表示数据的意义，所以我们通常使用字符串表示具体意义
# key必须是不可变数据类型(int,str,tuple)，因为不可变数据类型不可hash

# dict = {['a']:1,'key2':2}           # TypeError: unhashable type: 'list'


# ******************4、字典的增删改查*****************
# 可以增删改查表示该数据类型是可变数据类型

person_info= {'name':'江湖一笑','age':'一生一世'}
# 增
person_info['address'] = 'china'
print(person_info)          # {'name': '江湖一笑', 'age': '一生一世', 'address': 'china'}

# 删除
person_info.pop('name')
print(person_info)          # {'age': '一生一世', 'address': 'china'}


# 改
person_info['age'] = 200
print(person_info)          # {'age': 200, 'address': 'china'}

# 查
print(person_info['address'])           # china


# **********5、数据类型的序列和散列************
# 序列表示有序的数据str，list，tuple
# 散列表示无序的数据dict，set
tuple = (1,2)
print(tuple[1])

dict_seq = {'1':'1'}
print(dict_seq[0])          # KeyError: 0


# *************************************************************
# ****************6、列表字典在自动化测试中的应用********************
# *************************************************************
# 在以后的自动化测试中，我们存储一个测试用例，是用字典来存储的
# 存储多个测试用例使用列表存储的

case1 = {'host':'http://127.0.0.1:8080','method':'get','params':'data=100&page=2'}
case2 = {'host':'http://127.0.0.1:8080','method':'post','params':'data=100&page=2'}
case3 = {'host':'http://127.0.0.1:8080','method':'put','params':'data=100&page=2'}

cases = [case1,case2,case3]


