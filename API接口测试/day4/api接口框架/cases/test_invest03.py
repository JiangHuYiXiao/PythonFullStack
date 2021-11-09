# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/8 16:55
# @Software       : PythonFullStack
# @Python_verison : 3.7
'''

对我们的接口测试方法2，业务流方法的中的代码进行封装
封装方法1：数据预处理，读取excel中的数据，数据类型转换为字典

'''




import unittest

from jsonpath import jsonpath

from API接口测试.day4.api接口框架.common.API_Case import API_Case
from API接口测试.day4.api接口框架.common.read_excel import read_excel

from API接口测试.day4.api接口框架.config import config
from API接口测试.day4.api接口框架.config import user_info
import requests
from ddt import ddt,data
import json
invest_data = read_excel(file=config.testdata_file,sheetname='invest')

@ddt
class Test_Invest(unittest.TestCase,API_Case):
    @classmethod
    def setUpClass(cls):

        '''
        通过setUp获取投资人、借款人、管理员的登录信息，并且设置为类、对象属性，每个用例不一样所以写在setUp中
        在setUp中设置API_Case的属性，这类属性因为都是配置信息，所以，不需要通过jsonpath和setattr设置属性了
        :return:
        '''
        # 投资人手机号#investor_phone#
        cls.investor_phone = user_info.user['mobile_phone']
        # 投资人密码
        cls.investor_pwd = user_info.user['pwd']

        # 借款人手机号#loan_phone#
        cls.loan_phone = user_info.user['mobile_phone']
        # 借款人密码# loan_pwd#
        cls.loan_pwd = user_info.user['pwd']

        # 管理员手机号#admin_phone#
        cls.admin_phone = user_info.admin_user['mobile_phone']
        # 管理员密码#admin_pwd#
        cls.admin_pwd = user_info.admin_user['pwd']

    @data(*invest_data)
    def test_invest(self,info):
       self.steps(info)