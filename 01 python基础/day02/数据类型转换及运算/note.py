# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/9 15:28
# @Software       : PythonFullStack
# @Python_verison : 3.7
'''
# 数据类型转换
# 1、其他数据类型转换成str，基本上所有的数据类型都可以转换成str
# int --> str
# print(str(12),type(str(12)))     # <class 'str'>
#
# float -->str
# print(str(1.2334),type(str(1.2334)))   # <class 'str'>
#
# bool -->str
# print(str(False),type(str(False)))   # False <class 'str'>
#
# list -->str
# print(str([1, 2, 3]),type(str([1, 2, 3])))  # [1, 2, 3] <class 'str'>

# 2、其他类型转换成int，必须是一个整型的格式
# str-->int
print(type(int('12')),int('12'))            # <class 'int'> 12
# print(type(int('a')),int('a'))              # ValueError: invalid literal for int() with base 10: 'a'
# print(type(int('1.25')),int('1.25'))        # ValueError: invalid literal for int() with base 10: '1.25'

# float --> int   去掉小数部分
print(type(int(1.25)),int(1.25))            # <class 'int'> 1

# bool --> int
print(int(False),type(int(False)))          # 0 <class 'int'>

# 重点
# 3、其他类型转换成bool

# int --> bool 0为False，其他为True
print(type(bool(1)), bool(1))               # <class 'bool'> True
print(type(bool(1.36)), bool(1.36))               # <class 'bool'> True
print(type(bool(0)), bool(0))               # <class 'bool'> False

# str --> bool  只要不是空则结果都是True
print(type(bool('abe11')), bool('abe11'))           # <class 'bool'> True
print(type(bool('')), bool(''))           # <class 'bool'> False    空
print(type(bool(' ')), bool(''))           # <class 'bool'> True   空格
print(type(bool('0')), bool(''))           # <class 'bool'> True    0

# list --> bool   空为False
print(type(bool([1, 2])), bool([1, 2]))         # <class 'bool'> True
print(type(bool([])), bool([]))                 # <class 'bool'> False


# dict --> bool   空为False
print(type(bool({'a':1,'b':12})), bool({'a':1,'b':12}))         # <class 'bool'> True
print(type(bool({})), bool({}))                                 # <class 'bool'> False


# tuple --> bool   空为False
print(type(bool((12,'a'))), bool((12,'a')))         # <class 'bool'> True
print(type(bool(())), bool(()))                                 # <class 'bool'> False

# set --> bool   空为False
print(type(bool({1,2})), bool({1,2}))         # <class 'bool'> True
print(type(bool(set())), bool(set()))                                 # <class 'bool'> False


# 数据运算

    # 算数运算
print(1 + 2)        # 3
print(11 - 1)       # 10
print(11 * 10)   # 110
print(10 / 2)   # 相除 5.0
print(10 // 2)   # 整除 5
print(10 % 3)   # 取余  1
print(10 ** 3)  # 幂运算 1000
    # 赋值运算
a = 2
print(a)
a += 3    # 等价于a = a+2
print(a)
a -= 3
print(a)
'''

# 比较运算
a = 10
b = 20
print(a > b)        # False
print(a < b)        # True
print(a >= 10)      # True
print(a <= 10)      # True
print(a == 10)      # True
print(a != 10)      # False
# print(a <> 10)      # 3.7版本不支持
# 逻辑运算
# and :x and y,如果x为True，则返回y，x为 False 则返回x。0就是fasle，其他值就是true，如果x和y都为bool类型，则两个同为真则返回真，只要有一个为false，则返回false。
# or:x or y，如果x为True，则返回x，x为 False 则返回y。如果x和y都为bool类型，则只要有一个为false，则返回false，则只要有一个为true，则返回true。
# not:真返回假，假返回真。

# 逻辑运算优先级：
# () >not >and >or
# and
print(a and b)


# 成员运算
# 后续分解