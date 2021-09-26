# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/23 20:01
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目1
# 封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法) -
#
# 属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
#
# 方法一：计算总分，
#
# 方法二：计算三科平均分
#
# 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
#
# 请定义此类，并实例化1个学生,并打印学生个人信息，计算总分。


# class Student:
#     # 类属性
#     identity = '学生'
#
#     # 初始化方法
#     def __init__(self,name,age,gender,english_score,math_score,chinese_score):
#         # 实例属性
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.english_score = english_score
#         self.math_score = math_score
#         self.chinese_score = chinese_score
#
#     def sum_score(self):
#         '''
#         计算总成绩的方法
#         :return: 总成绩之和
#         '''
#         return(self.chinese_score + self.math_score + self.english_score)
#
#     def avg_score(self):
#         '''
#         计算学生英语、数学、语文的平均成绩
#         :return:
#         '''
#         return (self.sum_score()/3)
#
#     def info_student(self):
#         info = f'我的名字叫:{self.name}，年龄:{self.age},性别：{self.gender}。'
#         return info
#
# #实例化
# xiaoming = Student(name='xiaoming',age=16,gender='男',chinese_score=99,english_score=90,math_score=88)
#
# # 调用实例方法
# print('总分为:',xiaoming.sum_score())
# print(xiaoming.info_student())
# print(xiaoming.avg_score())




# 题目2：
#
# 定义一个类 Dog, 包含 2 个属性：名字和年龄。
#
# 定义一个方法 eat 吃东西。

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eating(self):
#         '''
#         吃东西的方法
#         :return: 正在吃东西
#         '''
#         return(f'{self.name}正在吃东西')
#
# # 实例化
# a_huang = Dog('阿黄',10)
#
# # 使用对象调用实例方法
# print(a_huang.eating())




# 题目3：定义一个登录的测试用例类LoginCase。每一个实例对象都是一个登陆测试用例。
#
# 属性：用例名称 预期结果 实际结果(初始化时不确定值哦)
#
# 方法：
#
# 运行用例
#
# 说明：有2个参数：用户名和密码。 能够登录成功的用户名：py37, 密码：666666。
#
# 通过用户名和密码正确与否来判断，是否登录成功。并返回实际结果。
#
# ps: 可以在用例内部考虑处理不符合的情况哦：密码长度不是6位/密码不正确/用户名不正确等。。
#
# 获取用例比对结果(比对预期结果和实际结果是否相等，并输出成功or失败)
#
# 实例化2个测试用例 ，并运行用例(调用方法) ，呈现用例结果(调用方法)

class LoginCase:
    # 类属性


    #初始化方法
    def __init__(self,case_name,case_expected,case_actual=''):
        self.case_name = case_name
        self.case_expected = case_expected
        self.case_actual = case_actual

    def run_case(self,name,password):
        '''

        :param name: 登录用户名称
        :param password: 登录用户的密码
        :return: 返回实际结果，或者出错时的用户名和密码
        '''

        # 进行异常判断
        try:
            # 用户名，密码正确
            if name == 'py37' and password == '666666':
                self.case_actual ='登录成功'
                if self.case_expected == self.case_actual:
                    print(f'用例{self.case_name}：执行成功,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                else:
                    print(f'用例{self.case_name}：执行失败,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                return self.case_actual
            # 密码长度不对
            elif len(password) != 6:
                self.case_actual ='登录失败'
                if self.case_expected == self.case_actual:
                    print(f'用例{self.case_name}：执行成功,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                else:
                    print(f'用例{self.case_name}：执行失败,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                return self.case_actual
            # 用户名或者密码不对
            elif name != 'py37' or password != '666666':
                self.case_actual ='登录失败'
                if self.case_expected == self.case_actual:
                    print(f'用例{self.case_name}：执行成功,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                else:
                    print(f'用例{self.case_name}：执行失败,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                return self.case_actual
            else:
                self.case_actual = '登录失败'
                if self.case_expected == self.case_actual:
                    print(f'用例{self.case_name}：执行成功,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                else:
                    print(f'用例{self.case_name}：执行失败,预期结果是:{self.case_expected},实际结果是:{self.case_actual}')
                return (name,password)
        except TypeError as e:
            print(f'数据类型错误{e}')


# 用例1：
L1 = LoginCase('test1','登录成功')
L1.run_case('py37','666666')


# 用例2
L2 = LoginCase('test2','登录成功')
L2.run_case('py137','e543543543@@@')

# 用例3
L3 = LoginCase('test3','登录成功')
L3.run_case('py137',999999)


L4 = LoginCase('test4','登录失败')
L4.run_case('py37','666666')




# 题目4：选作题（不需要提交)
# （不需要提交)

# 1.编写如下程序 编写一个工具箱类和工具类
#
# 工具类：需要有工具具的名称、功能描述、价格。
#
# 工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
#
# 实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
#
# 工具比如锤子、斧头、螺丝刀等工具。
#
# 提示：不需要用到继承。

class Tool:
    def __init__(self,name,info,price):
        self.name = name
        self.info = info
        self.price = price




class  ToolBox:
    def __init__(self,obj):
        self.obj = obj
    # 类属性：
    number = 0
    def add_tool(self,add_number):
        add_number = self.number + add_number
        print(f'添加{add_number}个工具到工具箱，总共有{add_number}个工具')
        return add_number

    def delete_tool(self,delete_number):
        delete_number = self.add_tool() - delete_number
        return (f'删除{delete_number}个工具从工具箱，总共有{delete_number}个工具')


    def select_tool(self):

        return (f'工具箱中有{self.number}个工具')

futou = Tool('斧头','砍柴',100)
res = print(ToolBox(futou).add_tool(1))

print(ToolBox(futou).delete_tool(1))
# chuizi = Tool('锤子','锤东西',100)
# print(ToolBox(chuizi).add_tool(1))
#
#
# luosidao = Tool('螺丝刀','拧螺丝',100)
# print(ToolBox(luosidao).add_tool(1))

# 不同方法、对象对同一个变量进行操作后，变量的值需要多次运算，怎么定义和操作有点模糊??
