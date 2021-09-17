# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/17 8:59
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、为啥要捕获异常：
# 我们目前在程序遇到错误时，后面的代码不会再执行了，导致后续的功能没法运行。
# 我们捕获异常是为了让程序遇到错误时，能够继续运行下去；
# age = input('请输入你的年龄：')
# if age:
#     next = age + 1
#     print('年龄有效')           # 上面的代码报错了，这行代码就不执行了


# 2、捕获一个异常
# 对可能出现异常的代码使用try


# try:
#     代码1     如果代码1有出现异常，name代码1后面的代码2、代码3都不会执行了，而是会立刻去执行except后面的代码
#     代码2
#     代码3
#     ...
# except ('异常类型')可选项 as e:     出现异常，立刻执行这个代码
#     输出异常信息或者出现异常你要做的任何操作
#     ...
# 处理异常后，这里的代码继续执行

 
age = input('请输入你的年龄：')
if age:
    try:
        next = age + 1
        print('年龄有效')           # 上面的代码报错了，这行代码就不执行了
    except:
        print('年龄无效')
    print('会执行吗')           # 上面的代码报错了，这里的代码会继续执行


age = input('请输入你的年龄：')
if age:
    try:
        next = age + 1
        print('年龄有效')           # 上面的代码报错了，这行代码就不执行了
    except TypeError as e:
        print(f'年龄无效,类型错误{e}')
    print('会执行吗')           # 上面的代码报错了，这里的代码会继续执行

# 年龄无效,类型错误can only concatenate str (not "int") to str
# 会执行吗

# 3、捕获多个指定的异常
age1 = int(input('请输入你的年龄：'))
name = 'jianghu'
if age1:
    try:
        next = age + 1
        print('年龄有效')           # 上面的代码报错了，这行代码就不执行了
    except TypeError as e:
        print(f'年龄无效,类型错误{e}')
    except SyntaxError as e:
        print(f'语法错误{e}')
    except NameError as e:
        print(f'名称错误{e}')
    print('会执行吗')           # 上面的代码报错了，这里的代码会继续执行



# 4、万能异常，前面的错误都不满足时候，执行这个万能异常
age1 = int(input('请输入你的年龄：'))
name = 'jianghu'
if age1:
    try:
        next = age + 1
        print('年龄有效')           # 上面的代码报错了，这行代码就不执行了
    except TypeError as e:
        print(f'年龄无效,类型错误{e}')
    except SyntaxError as e:
        print(f'语法错误{e}')
    except Exception as e:
        print(f'万能错误{e}')
    print('会执行吗')           # 上面的代码报错了，这里的代码会继续执行

# 5、异常的分类
# TypeError、SyntaxError、IndexError、NameError等等
# list = [12,122]
# print[list[1111]]
