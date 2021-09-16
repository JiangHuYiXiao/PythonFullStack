# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 9:31
# @Software       : PythonFullStack
# @Python_verison : 3.7
import random

# 1、随机整数
print(random.randint(1,22))

# 2、随机小数大于0小于1
print(random.random())

# 3、随机选择列表中的多个返回，返回的个数取决于第二个参数的值
print(random.sample([231,3242,'12'],3))         # [231, 3242, '12']
print(random.sample([231,3242,'12'],2))         # ['12', 3242]
print(random.sample([231,3242,'12'],1))         # [231]

# 4、打乱列表的顺序
item = [1,2,3,4,5,6]
random.shuffle(item)
print(item)