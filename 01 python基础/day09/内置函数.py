# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 9:02
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 内置函数：
# enumerate()   # 循环一个列表获取，索引和value,返回一个索引和value组成的元组
# eval()  去引号,也就是将字符串类型转换成其他类型
# zip()   把索引相同的数据组合在一起，生成一个zip对象，然后通过dict()可以将列表或者元组转换成字典(len必须一样),或者使用list(),tuple()转换成列表，元组
# id()        获取内存地址
# sum()       求和
# max()       最大值
# min()       最小值
for i in enumerate([1,2,4,5,77]):
    print(i)


for index,value in enumerate([1,2,4,5,77]):
    print(index,value)
    # 0 1
    # 1 2
    # 2 4
    # 3 5
    # 4 77

str= "('jianghuyixiao',111)"
str1= "1 + 55"
print(eval(str),type(eval(str)))    #    ('jianghuyixiao', 111) <class 'tuple'>
print(eval(str1),type(eval(str1)))    # 56 <class 'int'>


name = ['jianghu','yixiu','python']
age = [15,11,23]
print(zip(name, age))       # <zip object at 0x0000000000469AC8>
print(dict(zip(name, age)))    # {'jianghu': 15, 'yixiu': 11, 'python': 23}

tu1 = (1,2,4)
tu2 = ('a','b','c')
print(dict(zip(tu1,tu2)))           # {1: 'a', 2: 'b', 4: 'c'}
print(tuple(zip(tu1,tu2)))           # {1: 'a', 2: 'b', 4: 'c'}
print(list(zip(tu1,tu2)))           # {1: 'a', 2: 'b', 4: 'c'}

# int数据的内存地址
a = 11
print(id(a))            # 8790929757536
b = 11
print(id(b))            # 8790929757536
# 不可变(str,int,tuple,bool)数据类型的地址一样的，对于值一样的


# 列表数据的内存地址
list1 = [1,2]
list2 = [1,2]
print(id(list1))            # 3818440
print(id(list2))            # 8901128
# 可变数据类型(list,tuple,dict)的值一样时，内存地址id也是不一样的
