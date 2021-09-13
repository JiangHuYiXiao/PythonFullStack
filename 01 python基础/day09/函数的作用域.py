# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 9:01
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 作用域分类：
# 1、内置空间：就是我们python自带提供的内部空间，比如我们使用print()
# 2、全局空间:在文件中的顶格写的代码，也就是函数外的，
# 3、局部空间：函数内的，如果需要在局部空间修改全局变量，则需要在声明某个变量为全局变量，可以使用global进行声明

# 1、全局空间，不可以使用局部空间的变量，但是可以间接使用，比如使用函数return
a = 11
def out_func():
    b = 12
    print(b)

# print(b)            # NameError: name 'b' is not defined  全局空间，不可以使用局部空间的变量
out_func()

a = 11
def out_func():
    b = 12
    return b

print(out_func())      # 12

# 2、全局空间，不可以修改局部空间的变量
a = 11
def out_func():
    b = 12
    print(b)
b = b + 2
# print(b)            # NameError: name 'b' is not defined  全局空间，不可以修改局部空间的变量
out_func()


# 3、局部空间可以使用全局空间的变量
a = 11
def out_func():
    b = 12
    print(b + a)

out_func()          # 23


# 4、局部空间不可以修改全局空间的变量，但是可以通过global声明后修改
# a = 11
# def out_func():
#     b = 12
#     a = a + 100                 # UnboundLocalError: local variable 'a' referenced before assignment
#     print(b + a)
# out_func()


a = 11
def out_func():
    global a        # 声明a为一个全局变量
    b = 12
    a = a + 100
    print(b + a)
out_func()          # 123


# 一个函数内调用另一个函数，也可以调用本身（递归）
def eat(name,food):
    print('{}最喜欢吃{}'.format(name,food))

def offer(name,money,food):
    print('恭喜{}拿到{}k offer'.format(name,money))
    eat(name,food)              # 函数内调用另一个函数

offer('jianghu',26,'鸡肉')

# 函数体内调用函数本身
def run():
    print('hhhhh')
    run()
run()           # RecursionError: maximum recursion depth exceeded while calling a Python object


# 函数需要先定义后调用


def eat(name,food):
    print('{}最喜欢吃{}'.format(name,food))

offer('jianghu', 26, '鸡肉')     # NameError: name 'offer' is not defined

def offer(name,money,food):
    print('恭喜{}拿到{}k offer'.format(name,money))
    eat(name,food)              # 函数内调用另一个函数


# pycharm打断点不能打在函数定义

