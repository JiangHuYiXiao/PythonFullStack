# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 20:00
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 异常处理
# 题目：优化去生鲜超市买橘子程序
#
# a.收银员输入橘子的价格，单位：元／斤
#
# b.收银员输入用户购买橘子的重量，单位：斤
#
# c.计算并且 输出 付款金额
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况

# 请你说出常见的异常类型，并举个例子说明什么场景会遇到该异常类型。

def get_product_price(price,weight):
    try:
        int(price * weight)
        if price <= 0 or weight <= 0:                   # 没有异常的时候再去校验，是否为小于等于0的数字
            raise ValueError('价格或者重量不能小于等于0')
    except ValueError as e:
        print(f'值错误{e}')
    except TypeError as e:
        print(f'数据类型错误{e}')

    return price * weight
print(get_product_price(1,2))
print(get_product_price('',2))
print(get_product_price([],2))
print(get_product_price('abc',2))
print(get_product_price(0,2))
print(get_product_price(-9,2))