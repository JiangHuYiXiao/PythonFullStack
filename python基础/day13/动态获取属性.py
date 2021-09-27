# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/26 20:36
# @Software       : PythonFullStack
# @Python_verison : 3.7

# setattr()         设置属性，属性名称是字符串，这样，我们可以让用户输入，这样就是一个动态的。
# getattr()         获取属性

class Mobile:
    call_atr = '可以'
    color_atr = '五彩斑斓'

    def __init__(self,color,brand):
        self.color = color
        self.brand = brand


    def call(self):
        print('正在打电话')


    def take_picture(self):
        print('正在拍照')


    def record(self):
        print('正在录制')

# 获取属性的方法：
# 类.属性名称
print(Mobile.call_atr)                      # 可以

# 通过getattr()
print(getattr(Mobile, 'call_atr'))          # 可以

input_str = input('请输入你的属性名称：')
print(getattr(Mobile, input_str))


# 设置属性的方法

# 类.属性名称 = value

Mobile.call_atr = 'No'
print(Mobile.call_atr)

setattr(Mobile,'call_atr','hello china')
print(getattr(Mobile, 'call_atr'))

# 可以
# 可以
# 请输入你的属性名称：color_atr
# 五彩斑斓
# No
# hello china
