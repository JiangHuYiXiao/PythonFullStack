# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/20 9:39
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、实例化

# 为啥我们类后面加上括号就是一个对象？
# 因为我们使用Car()就是一个创建对象的过程，在创建对象的过程也叫作实例化过程，
# 在实例化过程的步骤是：
    # 先调用__init__(self)方法，所有的类默认都有一个__init__方法，叫做初始化函数
    # __init__(self)方法，我们可以自己重写，这样的话，我们可以自己定义初始化的一个过程

    # 再去执行类中的代码块
'''
class Car:
    element = '钢材'

    def __init__(self,color,logo):          # 自己定义一个初始化的过程
        # self.color =color
        # self.logo =logo
        print('一个car对象的产生过程')
        print('第一步装底盘')
        print('第二步装车架')
        print(f'喷了{color}的漆')
        print(f'印了{logo}的logo')


my_car = Car('黄色','本田')             # 实例化
print(my_car)

# 这样是没法通过对象获取color的，因为color现在就是一个简单的函数的参数，不是任何属性
# print(my_car.color)         # AttributeError: 'Car' object has no attribute 'color'

# __init__(self)函数没有返回值，为None，
# __init__(self,arg1,arg2,....)可以添加参数


# *************************self*****************************
# self的作用:在对象的生产过程中，代表即将生产的对象的一个标记
# self的作用域：是类里面的，那么类外面是没有这一个self的
# ******************************************************



# 2、# 3、实例化过程，self.color ='红色'，self.logo ='保时捷'，实例属性永远都是红色、保时捷
class Car:
    # 类属性
    element = '钢材'

    def __init__(self,color,logo):          # 自己定义一个初始化的过程

        # 这里的color，logo就是实例属性
        # 这样写的话，不管传的是什么值，color，logo永远不变
        self.color ='红色'
        self.logo ='保时捷'
        print('一个car对象的产生过程')
        print('第一步装底盘')
        print('第二步装车架')
        print(f'喷了{color}的漆')
        print(f'印了{logo}的logo')

# init这样定义的话我们color属性永远是红色
# init这样定义的话我们logo属性永远是保时捷


my_car = Car('黄色','本田')             # 实例化
print(my_car)

# 这样获取的是实例属性
print(my_car.color)     # 红色
'''




# 3、实例化过程，self.color = color，self.logo = logo，实例属性跟着实例化时参数的改变而改变

class Car:
    # 类属性
    element = '钢材'

    def __init__(self,color,logo):          # 自己定义一个初始化的过程
        # 这里的color，logo就是实例属性
        # 这样写的话，传的是什么值，color，logo跟着变化
        # 类里面获取实例属性
        self.color = color
        print(id(self.color))           # 6143032
        self.logo = logo
        print('一个car对象的产生过程')
        print('第一步装底盘')
        print('第二步装车架')
        print(f'喷了{color}的漆')
        print(f'印了{logo}的logo')

# init这样定义的话我们color属性就是和传参跟着变化
# init这样定义的话我们logo属性永远是保时捷和传参跟着变化


my_car = Car('黄色','本田')             # 实例化，
print(my_car)

# 类外面获取实例属性
print(my_car.color)     # 黄色

# self和my_car是相等的,只是一个是类里面，一个是在类外面
print(id(my_car.color))         # 6143032