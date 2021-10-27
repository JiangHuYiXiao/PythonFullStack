# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 20:42
# @Software       : PythonFullStack
# @Python_verison : 3.7


# excel结合测试用例的用法
# 1、为什么要用excel单独管理用例？
    # 便于维护

# 2、具体用法
# 通过read_excel_dict进行数据读取
# 通过参数化完成数据到用例的结合
# 用例函数只需要写一个，但是测试数据有多个，则测试用例有多个
# 只有业务逻辑一样，但是测试数据不一样的才可以整合到一个用例函数中，然后使用ddt进行数据驱动


# 3、注意事项
# excel中不存在字典，读取出来的数据是字符串，需要通过eval()进行去引号
# 参数化不要用for循环，因为for循环，如果有多个测试数据，只能统计到一个测试用例，且遇到用例失败后，后面的用例不会再继续执行了。


# 4、参数化vs 数据驱动
    # 参数化是函数的参数，也就是测试数据
    # 数据驱动是一种测试思想


# 5、编写测试用例函数的步骤

    # 1、获取测试数据，通过前面封装的read_excel_dict函数读取excel中的内容
    # 2、编写测试login的类，准备预期结果
    # 3、调用函数login得到实际结果
    # 4、对预期结果和实际结果进行断言
