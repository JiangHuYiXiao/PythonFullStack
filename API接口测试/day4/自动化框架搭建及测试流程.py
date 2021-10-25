# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/22 9:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

# *******************项目中自动化测试框架搭建流程********************

# 1、测试框架搭建

    # 1.1、使用分层设计思想，创建不同的目录存放不同类型的文件，便于后续项目中用例文件修改和维护
    # 1.2、创建不同包、目录文件
        # cases  存放测试用例包
        # data 存放测试用例数据包
        # common  存放通用功能包
        # report  存放测试报告文件夹
        # run.py   执行测试用例文件
        # config   配置文件夹
    # 1.3、自动化测试框架解决了哪些问题
        # 数据驱动
        # 数据库数据断言
        # 数据读取
        # 动态参数获取



# 2、自动化测试流程
    # 2.1、需求分析，（需求文档、接口文档）
    # 2.2、测试计划（可行性分析、自动化测试框架使用哪个unittest、pytest、时间管控、人员管控、技术管控、风险分析等）
    # 2.3、用例编写（先执行手动用例，然后看哪些用例需要执行自动化测试）

    # **********************************************************************
        # 注意在excel中的数据读取出来都是字符串，必须使用双引号
        # 在excel中为空时如果调用接口返回的是None，在excel中必须写成null，在python编写时必须写成None
    # **********************************************************************

    # 2.4、评审
    # 2.5、执行
    # 2.6、测试报告输出



# 3、自动化测试的应用
    # 冒烟
    # 回归
    # 持续集成


# 4、代码调试

# 1、当一个数据不知道结果是多少时，我们需要这个数据产生前面打断点
# 2、使用ddt代码调试时，运行用例文件时需要执行class上的运行图标，不要点用例上面的

# 5、报告文件每次执行新生成一个文件根据日期时间格式

# 在run.py文件中使用，datetime模块