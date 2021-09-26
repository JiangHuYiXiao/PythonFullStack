# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/24 10:06
# @Software       : PythonFullStack
# @Python_verison : 3.7

class Mobile:
    '''
    对于分不清什么属性用类属性，什么属性用实例属性，
    对于每个对象值都一样的我们定义类属性
    对于每个对象值都不一样的我们定义实例属性
    或者我们统一刚开始都定义为实例属性，后面发现属性的值不变的时候，我们可以再把它定义为类属性。
    '''
    # 类属性，所有手机都可以打电话
    can_call = True
    # 初始化方法
    def __init__(self,color,brand):
        # init没有返回值
        # 实例属性
        self.color = color
        self.brand = brand

    # 实例方法
    def call(self):
        print('正在打电话')
    def sell(self,price):
        print(f'手机卖了{price}钱')
        return price
    # 实例方法
    def take_picture(self):
        # 在方法中使用类属性，self.属性
        print(f'{self.brand}手机正在拍照')

    def record(self):
        print('正在录音')
        self.call()

    # 类方法
    @classmethod
    def cls_func(cls):
        print('这是一个类方法')


    # 静态方法
    @staticmethod
    def package():
        print('正在打包')


# 继承了父类所有的属性和方法
class SmartMobile(Mobile):
    pass

# 方法
SmartMobile('黑色','xiaomi').call()           # 正在打电话

# 属性
print(SmartMobile('黑色', 'xiaomi').can_call)     # True