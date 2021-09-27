# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 超继承表示子类重写父类Mobile的call方法,并且使用super()进行表标记超继承，这样，我们使用call()方法时，先运行父类的额，然后再运行自己的。
# super().call()


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

    # 在子类重写父类Mobile的call方法,并且使用super()进行超继承，这样，我们使用call()方法时，先运行父类的额，然后再运行自己的。

    def call(self):
        super().call()
        print('智能手机边电话边做其他事')

SmartMobile('蓝色','荣耀').call()