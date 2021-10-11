# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/11 9:24
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、读取yaml文件需要
    # 1、安装PyYaml
    # 2、导入yaml
import yaml

with open('demo.yaml',encoding='utf-8') as file:
    data = yaml.safe_load(file)

print(data)
# 读取出来是一个字典的数据类型
# {'username': 'jianghu', 'password': 123456, 'list1': [1, 2, 4], 'list2': [1, 2, 4], 'dict1': {'age': 18, 'name': 'jianghuyixiao'}, 'dict2': {'id': 1, 'age': 12, 'name': 'yaya'}}



# #数字
# password: 123
#
# # 字典
# #方式1
# dict1: {'age':18,'name':'jianghuyixiao'}
#
# #方式2
# dict2:
#   'age': 12   冒号后必须有一个空格
#   'name': 'yaya'
#
# #列表
#
# #方式1
# list1: [1,2,'jianghu','xiaoming']
#
#
# #方式2
# list2:
#   - 1
#   - 2
#   - 3

# 2、读取yaml字符串内容
str1='''
list3:
  - 'a'
  - 11
'''
print(yaml.load(str1, Loader=yaml.FullLoader))       # {'list3': ['a', 11]}


str2='''

- 
  list4:
    - 'a'
    - 11
'''
print(yaml.load(str2, Loader=yaml.FullLoader))       # {'list3': ['a', 11]}