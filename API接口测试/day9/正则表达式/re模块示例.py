# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/6 13:22
# @Software       : PythonFullStack
# @Python_verison : 3.7


import re
string= '{"member_id":"#member_id#","amount":#money#}'
class Data:
    # 这里的属性名称必须和excel中的#名称#中的名称一样
    member_id ='123456'
    money = 600

result = re.finditer('#(.*?)#',string)             # 这个函数获取的是所有的# #
# print(result)               # <callable_iterator object at 0x0000000002338B70>可迭代对象
# 所以使用for循环处理
for el in result:
    # print(el.group())           # #member_id#    #money#
    # print(el.group(1))          # member_id     money
    old = el.group()
    new = getattr(Data,el.group(1))
    string = string.replace(old,str(new))
print(string)