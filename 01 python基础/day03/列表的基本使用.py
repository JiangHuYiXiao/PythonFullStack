# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 18:56
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、列表的定义：[]
# li = [1,23,333]

# 2、列表的作用，存储有序的数据
# 列表中可以包含任意的数据类型
li = [1,23,'333',[112,110],{'a':1},(1,23)]

# 3、列表的索引
# 从0开始和字符串样
li =[1,2,'jianghu','hello']
print(li[0])            # 1
print(li[-1])            # hello
print(len(li))          # 4

# 超过最大索引报错
# print(li[len(li)])          # IndexError: list index out of range

# 4、列表的切片
# [start,end,step],start,end可以为负数，step默认等于1,包头不包尾
print(li[0:2])          # [1,2]
# 取后两位
print(li[-2:])          # ['jianghu', 'hello']

print(li[-3:-1])

print(li[9:])               # 切片超过最大索引不报错           []
print(li[0:555])               # 切片超过最大索引不报错        [1, 2, 'jianghu', 'hello']


# 5、列表的嵌套

list = [1,2,3,[4,5]]
print(list[-1][0])          # 4


# 6、列表的操作（增，删，改，查）
# *********************************列表的所有操作都是在原先的列表上操作，因为列表是可变数据类型*********************************

# 1、*********增***********
list1 = [1,2,3,'hello',{'key1':9999}]

# append()在原有的列表最后添加
list1.append(222)
print(list1)            # [1, 2, 3, 'hello', {'key1': 9999}, 222]


# insert(index,value)    在索引index处插入值
list1.insert(1,'first')
print(list1)            # [1, 'first', 2, 3, 'hello', {'key1': 9999}, 222]

# extend()  添加多个值

list1.extend(['CBA','NBA'])
print(list1)            # [1, 'first', 2, 3, 'hello', {'key1': 9999}, 222, 'CBA', 'NBA']

# 2、*********删*********

# remove()   删除指定的值，如果值不存在删除报错,没有返回值
list1.remove('CBA')
print(list1)            # [1, 'first', 2, 3, 'hello', {'key1': 9999}, 222, 'NBA']

# list1.remove('sdfdsdf')
# print(list1)            # ValueError: list.remove(x): x not in list

# pop()根据索引删除,返回被删除的元素
print(list1.pop(1))         #
print(list1)            # [1, 2, 3, 'hello', {'key1': 9999}, 222, 'NBA']


# 3、**********修改*********
list1[-1] = 'WNBA'
print(list1)            # [1, 2, 3, 'hello', {'key1': 9999}, 222, 'WNBA']


# 4、***********index()获取索引**********

print(list1.index('WNBA'))          # 6