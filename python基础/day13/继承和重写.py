# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:13
# @Software       : PythonFullStack
# @Python_verison : 3.7

class Mobile:
    call = True

    def __init__(self,color,brand):
        self.color = color
        self.brand = brand


    def call(self):
        print('正在打电话')


    def take_picture(self):
        print('正在拍照')


    def record(self):
        print('正在录制')

class Play:
    def chiji(self):
        print('玩吃鸡游戏')




# 单继承
class SmartMobile(Mobile):
    print('这是一个智能手机')

    # 在子类重写父类Mobile的call方法
    def call(self):
        print('智能手机边电话边做其他事')


# 多继承
class SmartMobilePlay(Mobile,Play):
    print('这是一个可以玩游戏的智能手机')

    # 在子类重写父类Mobile的call方法
    def call(self):
        print('智能手机边电话边做其他事')






SmartMobile('黑色','荣耀').call()           # 因为自己这个类中有call方法，所以先用自己的call
SmartMobile('红色','oppo').take_picture()         # 因自己这类没有record方法，所以就去找父类的
SmartMobilePlay('蓝色','华为').chiji()              # 玩吃鸡游戏