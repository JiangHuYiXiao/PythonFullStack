# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:09
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 类方法、实例方法、静态方法的区别？

# 定义：
    # 类方法：是在类里面使用@classmethod装饰器装饰，并且默认参数为cls的一个方法。

    # 实例方法：在类中，然后默认参数为self的方法。

    # 静态方法：在类中，使用@staticmethod装饰器装饰的，没有默认参数的一个方法，这个方法和类对象没有太大关系，只是一般把他放在类中而已。

# 调用：

# 类方法：对象.方法名()  类.方法名()

# 实例方法：对象.方法名()

# 静态方法：类.方法名()  对象.方法名()

class Mobile:
    @classmethod
    def c_func(cls):
        pass

    def func(self):
        pass

    @staticmethod
    def static_func():
        pass

# 类方法

Mobile().c_func()
Mobile.c_func()

# 实例方法：只能使用对象调用
# Mobile.func()           # TypeError: func() missing 1 required positional argument: 'self'

Mobile().func()


# 静态方法
Mobile().static_func()

Mobile.static_func()