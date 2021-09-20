# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/20 8:27
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、类的定义：具备共同特征和行为的事物的总称。
# 特征对应属性
# 行为对应方法
# 类是虚拟不存在的，是一个概括
# 类名称需要使用大驼峰的命名法，单词首字母大写


class Car:
    color = '黄色'
    wheel = True
    drrived = True
    # print(color)
    # print(f'color：{color}')         # color：黄色   类里面使用类属性
    # print(f'颜色：{color}')            # 颜色：黄色



# 2、类的调用---->类名称

# print(Car)          # <class '__main__.Car'>   表示一个类



# 3、类属性，也就是类变量,在类作用域下的变量
# color就是一个类属性，类变量



# *************类外面调用类属性************
# 类属性的调用：类名称.属性
# print(Car.color)            # 黄色
# print(Car.wheel)            # True

# 这样获取不了，因为这样写，那么color必须是全局变量，顶格写
# print(color)


# *************类里面调用类属性************
#     print(f'color：{color}')  # color：黄色   类里面使用类属性
#     print(f'颜色：{color}')  # 颜色：黄色



# ************类属性的修改************
Car.color = '绿色'
print(Car.color)            # 绿色




# *************通过对象获取类属性*******************
my_car= Car()
p2_car= Car()
print(my_car.color)         # 绿色，上面的类属性一改，所有对象的属性都被修改了
print(p2_car.color)         # 绿色，上面的类属性一改，所有对象的属性都被修改了



# 4、对象的定义
# 对象是类的一个实体，实例，是类的一个组成成员
# 比如Car中的，我的车，丰田车这都是一个实实在在的实体
# 对象的产生:类名称()
# 对象命名使用小驼峰
# 对象也叫做实例

# my_car = Car()
# print(my_car)           # <__main__.Car object at 0x000000000075F7F0>

# 5、不同的对象内存地址是不一样的
# your_car = Car()
# print(your_car == my_car)           # False
#
# print(Car() == Car())               # False



# 6、对象属性，某个实例或者成员的属性，个体属性，定义是：对象.类变量  --->p1_car.wheel
p1_car = Car()
print(p1_car.wheel)         # 这是通过对象获取类属性   True

# 对象属性
p1_car.wheel = False        # 修改对象属性，这样只改了对象自己的，整个类的属性是没有改的
p1_car.chinese = '牛逼'
print(p1_car.wheel)         # False
print(p1_car.chinese)         # 牛逼


# 类属性
print(Car.wheel)            # True  还是True

