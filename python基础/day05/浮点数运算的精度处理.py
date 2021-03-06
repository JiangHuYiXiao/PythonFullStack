# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 8:55
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、python中对于浮点数的运算，可能会存在精度运算问题，出现的概率也是随机的。
# 如果精度有问题使用Decimal类进行处理
from decimal import Decimal


a = 0.2
b = 0.2
print(0.3 + 0.3)            # 0.6
print(0.3 + 0.6)            # 0.8999999999999999
# ****************************************************
# ***使用Decimal,需要注意点是，传入的数据必须是字符串类型**
# ****************************************************
print(Decimal('0.3')+ Decimal('0.6'))

# 经常用于浮点数的运算处理，在自动化测试中对浮点数的判断都需要使用Decimal进行断言

