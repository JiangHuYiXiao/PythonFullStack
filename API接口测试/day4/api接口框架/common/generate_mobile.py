# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/27 15:24
# @Software       : PythonFullStack
# @Python_verison : 3.7

from faker import Faker
def generate_cell():
    '''
    生成一个手机号码
    :return: 手机号码
    '''
    faker = Faker(locale=['zh-cn'])
    return faker.phone_number()