# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/18 9:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目：实例属性怎么定义？
# 类里面：
    # self.arg1 = arg1

# 类外面：
    # 实例.属性名 = 属性名
    # s1.age = age



# 题目：实例方法中的self代表什么？（简答）

    # 代表对象的生产过程中的，即将生产对象的一个标记
    # self的内存地址和实例化时对象的内存地址是一样的

# 题目：类中__init__方法在什么时候会调用的？（简答）
#     对象生成的时候
#         类名()


# 题目：
#
# 封装一个学生类Student，(自行分辨定义为类属性还是实例属性
#
# 属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩

class Student:
    # 类属性
    identity = '学生'

    def __init__(self,name,age,gender,english_score,math_score,chinese_score):
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender
        self.english_score = english_score
        self.math_score = math_score
        self.chinese_score = chinese_score


xiaoming = Student(age=18,name='小花',gender='女生',english_score='100',math_score=99,chinese_score='89')
print(xiaoming.identity)            # 学生
print(xiaoming.name)            # 小花
print(xiaoming.age)                 # 18



