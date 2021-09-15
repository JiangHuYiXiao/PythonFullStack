# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 15:02
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 字典
# 题目：使用字典和列表存储和操作以下数据
#
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
#
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
#
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
#
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
#
# e, 你进一步添加自己的兴趣，兴趣至少包含 3个(注意：兴趣是另外一个列表。请将这个列表作为一个成员，添加到原个人信息列表当中，添加到末尾即可。

# person_info = {'name':'一休小和尚','性别':'男','年龄':19}
# person_info['身高'] = 175
# person_info['cellphone'] = '182020211111'
# person_info.pop('cellphone')
# print(person_info)
# person_info['star_name'] = '花和尚'
# person_info['身高'] =180
# person_info['兴趣'] = ['python','美食','运动']
# print(person_info)


# 数据类型
# 题目（字符串和列表）：利用下划线将列表li=["python","java","php"]的元素拼接成一个字符串，然后将所有字母转换为大写。
# PYTHON_JAVA_PHP

# 方法1 使用字符串的join()函数,通过特定的拼接符，将列表拼接成字符串
# li=["python","java","php"]
# res  = '_'.join(li)
# print('_'.join(li))
# print(res.upper())
#
# # 方法2：使用f_string,进行格式化拼接
# a = li[0]
# b = li[1]
# c = li[2]
# str = f'{a}_{b}_{c}'
# print(str)
# print(str.upper())


# 还可以使用+，或者format进行拼接




# 题目（类型操作）有下面几个数据 ：
# t1 = ("aa",11)
# t2= ("bb",22)
# li1 = [("cc",11)]
# 请通过学过的知识点，进行相关操作变为如下字典:

# {"aa":11,"cc":11,"bb":22}
# 提示：元组取值，然后给字典添加key-value

t1 = ("aa",11)
t2= ("bb",22)
li1 = [("cc",11)]
dict = {}
key1 = t1[0]
key2 = t2[0]
key3 = li1[0][0]
dict[key1] = t1[1]
dict[key2] = t2[1]
dict[key3] = li1[0][1]
print(dict)








# 把列表形式的用例转化成字典格式：

# 题目：列表和字典数据类型转换
#
# # 有一组用例数据如下：
# cases = [
#   ['case_id', 'case_title', 'url', 'data', 'excepted'],
#   [1, '用例1', 'www.baudi.com', '001', 'ok'],
#   [4, '用例4', 'www.baudi.com', '002', 'ok'],
#   [2, '用例2', 'www.baudi.com', '002', 'ok'],
#   [3, '用例3', 'www.baudi.com', '002', 'ok'],
#   [5, '用例5', 'www.baudi.com', '002', 'ok'],
# ]
# ​
# # 要求一：把上述数据转换为以下格式
# res1 = [
#   {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#   {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]

cases = [
  ['case_id', 'case_title', 'url', 'data', 'excepted'],
  [1, '用例1', 'www.baudi.com', '001', 'ok'],
  [4, '用例4', 'www.baudi.com', '002', 'ok'],
  [2, '用例2', 'www.baudi.com', '002', 'ok'],
  [3, '用例3', 'www.baudi.com', '002', 'ok'],
  [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 方法1：每个元素单独获取
# res1 = []
# dict1 = {cases[0][0]:cases[1][0],cases[0][1]:cases[1][1],cases[0][2]:cases[1][2],cases[0][3]:cases[1][3],cases[0][4]:cases[1][4]}
# res1.append(dict1)
# dict2 = {cases[0][0]:cases[2][0],cases[0][1]:cases[2][1],cases[0][2]:cases[2][2],cases[0][3]:cases[2][3],cases[0][4]:cases[2][4]}
# res1.append(dict2)
# dict3 = {cases[0][0]:cases[3][0],cases[0][1]:cases[3][1],cases[0][2]:cases[3][2],cases[0][3]:cases[3][3],cases[0][4]:cases[3][4]}
# res1.append(dict3)
# dict4 = {cases[0][0]:cases[4][0],cases[0][1]:cases[4][1],cases[0][2]:cases[4][2],cases[0][3]:cases[4][3],cases[0][4]:cases[4][4]}
# res1.append(dict4)
# dict5 = {cases[0][0]:cases[5][0],cases[0][1]:cases[5][1],cases[0][2]:cases[5][2],cases[0][3]:cases[5][3],cases[0][4]:cases[5][4]}
# res1.append(dict5)
# print(res1)
# 方法2：使用for循环
# res1 = []
# keys = cases[0]
# for j in range(len(cases) -1):
#   values = cases[j + 1]
#   dict = {keys[i]:values[i] for i in range(len(keys))}
#   res1.append(dict)
# print(res1)
# 方法3：使用zip()、dict()函数将两个索引数相同的列表转换成字典
# def list_to_dict():
#   li1 = cases[0]
#   res = []
#   for i in range(len(cases)-1):
#     li2 = cases[ i+ 1]
#     res.append(dict(zip(li1, li2)))
#   return res
#
# print(list_to_dict())
