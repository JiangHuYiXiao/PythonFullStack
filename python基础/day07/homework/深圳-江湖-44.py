# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/10 9:42
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目1：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：
# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。

def product_discount(price):
    if 0<= price < 50:
        discount = 1
        dis_price = price * discount
        return(f'你的商品金额为{price}:折扣为{discount}:实际付款金额为{dis_price}')
    elif (50 <= price <= 100):
        discount = 0.9
        dis_price = price * discount
        return(f'你的商品金额为{price}:折扣为{discount}:实际付款金额为{dis_price}')

    elif (price > 100):
        discount = 0.8
        dis_price = price * discount
        return(f'你的商品金额为{price}:折扣为{discount}:实际付款金额为{dis_price}')
    else:
        return('价格错误')


print(product_discount(88))
print(product_discount(8))
print(product_discount(118))
print(product_discount(-888))



# 题目2：列表去重函数 定义一个函数 def remove_element(a_list):，
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素。
#
# def remove_repeatitive_elements(a_list):
#   ...​
# my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
#
# remove_repeatitive_elements(my_list)

def remove_element(a_list):
    '''
    列表去重函数
    :param a_list:
    :return:
    '''
    return (set(a_list))


my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(remove_element(my_list))



# 题目3：通过定义一个计算器函数，调用函数传递两个数据和操作， 然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
#

def calculate1(a, b, action):
    '''

    :param a:
    :param b:
    :param action:
    :return:
    '这是一个计算器函数，选择action为1加法运算，为2减法运算，为3乘法运算，为4除法运算'
    '''
    if action == 1:
        return(a + b)
    if action == 2:
        return(a -b)
    if action == 3:
        return(a * b)
    if action == 4:
        return (a / b)

print(calculate1(1, 2,1))
print(calculate1(1, 2,2))
print(calculate1(1, 2,3))
print(calculate1(1, 2,4))



def calculate2(a, b, *args):
    '''

    :param a:
    :param b:
    :param action:
    :return:
    '这是一个计算器函数，选择action为1加法运算，为2减法运算，为3乘法运算，为4除法运算'
    '''
    action = int(input('请输入你的action为1加法运算，为2减法运算，为3乘法运算，为4除法运算:'))
    if action == 1:
        return(a + b)
    if action == 2:
        return(a -b)
    if action == 3:
        return(a * b)
    if action == 4:
        return (a / b)







