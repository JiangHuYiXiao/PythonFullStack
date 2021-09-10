# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/9 20:18
# @Software       : PythonFullStack
# @Python_verison : 3.7
# 函数定义：
# def 函数名称(可选参数1，可选参数2)：  # 函数名称命名规则必须符合变量命名规则，名称尽量做到见名知意
    # 函数体
    # return 返回值（可选）

# 例子:
# def test_hello():
#     print('hello world')

# 函数的作用:为了封装，把一些功能封装在函数中，后续使用时候可以重复使用，容易维护。

# 函数的调用：
# 函数名称()

# return的作用
# 返回值
# 终止函数调用
'''
# return返回值的分类
# 1、如果函数定义时没有返回值return，则调用函数时，返回None
def add():
    a = 1
    b = 4
    c = a + b
add()       # 不打印的话是没有值的

print(add())    # None


# 2、函数有返回值，则范湖调用时，返回的结果需要根据函数定义时的return来
def add():
    a = 1
    b = 4
    return(a + b)
add()       # 不打印的话是没有值的
print(add())   # 5


# 3、如果函数有多个return则只会执行第一个return
def add():
    a = 1
    b = 4
    return(a + b)
    return('aaaa')    # 不执行
add()       # 不打印的话是没有值的
print(add())   # 5

'''
# 3、有多少返回值，用多少个变量接收,如果不接收默认返回一个元组

def add():
    a = 1
    b = 4
    return(a,b,a + b)


add()       # 不打印的话是没有值的
print(add())   # (1, 4, 5)
i,j,c = add()
print(i,j,c)


# 函数的参数
# 如果根据函数定义和调用来说，分为形参和实参
# 如果根据函数定义来说分为位置参数、默认参数，可变位置参数*args返回结果是一个元组，可变关键字参数**kwargs，返回结果是一个字典
# 如果根据函数调用来说的话，分为位置参数，关键字参数，但是位置参数必须放在前面

# 1、形参，实参
def test_func(a,b):  # a,形参，b，形参
    return(a + b)


print(test_func(1,2))   # 1,2 实参


# 2、位置参数
def test_func(a,b):  # a,b，位置参数
    return(a + b)
print(test_func(1,2))   # 1,2 也是位置参数


# 3、关键字参数
def test_func(a,b):  # a,b，位置参数
    return(a + b)
print(test_func(a=1,b=2))   # 1,2 关键字参数


# 4、默认参数
def test_func(a,b=4):  # a,位置参数,b是默认参数
    return(a + b)
print(test_func(a=1))   # 1 关键字参数


# 5、可变位置参数*args，
def test_func(a,b,*args):  # a,b，位置参数且是必填的  *args为可选，多个位置参数,返回一个元组
    return(a + b,args)
print(test_func(a=1,b=2))   # 1,2 关键字参数     结果是(3, ()),返回一个元组
print(test_func(1,2,3,5))   # 1,2 关键字参数，3,5则是可变的位置参数， 结果是(3, (3, 5)),返回一个元组


# 6、可变关键字参数**kargs，
def test_func(a,b,**kwargs):  # a,b，位置参数且是必填的  **kargs为可选，多个关键字参数
    return(a + b,kwargs)
print(test_func(a=1,b=2))   # 1,2 关键字参数     结果是(3, {}),返回一个元组包含字典
print(test_func(1,2,key1=33,key2= 44))   # 1,2 关键字参数，3,5则是可变的位置参数， 结果是(3, {'key1': 33, 'key2': 44}),返回一个元组包含字典


# 7、函数调用时位置参数必须在最前面
def test_func(a,b,*args,**kwargs):  # a,b，位置参数且是必填的  **kargs为可选，多个关键字参数
    return(a + b,args,kwargs)
print(test_func(a=1,b=2))   # 1,2 关键字参数     结果是(3, (), {}),返回一个元组包含字典，元组
print(test_func(1,2,'aaa',key1=33,key2= 44))   # 1,2 关键字参数，3,5则是可变的位置参数， 结果是(3, ('aaa',), {'key1': 33, 'key2': 44}),返回一个元组包含字典,元组