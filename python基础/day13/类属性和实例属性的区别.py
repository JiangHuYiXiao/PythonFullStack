# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:07
# @Software       : PythonFullStack
# @Python_verison : 3.7


# 类属性和实例属性的区别？

# 1、作用域
# 类属性是类中所有对象的且类属性一般是不变化的，实例属性是每个实例自己的是根据实例来的是变化的。

# 2、调用方式
# 类属性可以使用类调用，也可以使用对象进行调用
# 实例属性只能使用对象进行调用
class A:
    a = 1
    def __init__(self,b):
        self.b = b

    def func(self):
        pass

# 类属性：
print(A.a)
print(A(2).a)



# 实例属性：
print(A(2).b)
print(A.b)          # AttributeError: type object 'A' has no attribute 'b'