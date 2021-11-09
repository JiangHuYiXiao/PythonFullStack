# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/8 16:55
# @Software       : PythonFullStack
# @Python_verison : 3.7

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

    # def setUp(self):
    #
    #     '''
    #     通过setUp获取投资人、借款人、管理员的登录信息，并且设置为类、对象属性，每个用例不一样所以写在setUp中
    #     在setUp中设置API_Case的属性，这类属性因为都是配置信息，所以，不需要通过jsonpath和setattr设置属性了
    #     :return:
    #     '''
    #     # 投资人手机号#investor_phone#
    #     API_Case.investor_phone = user_info.user['mobile_phone']
    #     # 投资人密码
    #     API_Case.investor_pwd = user_info.user['pwd']
    #
    #     # 借款人手机号#loan_phone#
    #     API_Case.loan_phone = user_info.user['mobile_phone']
    #     # 借款人密码# loan_pwd#
    #     API_Case.loan_pwd = user_info.user['pwd']
    #
    #     # 管理员手机号#admin_phone#
    #     API_Case.admin_phone = user_info.admin_user['mobile_phone']
    #     # 管理员密码#admin_pwd#
    #     API_Case.admin_pwd = user_info.admin_user['pwd']
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
        # print(info)
        # 1、读取excel中的数据，预期结果
        headers = info['headers']
        str_data = info['json']
        method = info['method']
        url = config.host + info['url']
        expected = json.loads(info['expected'])

        # 使用replace_data替换excel中的#...#数据
        # 在使用正则表达式进行替换时候，必须先设置类属性，且名称和excel中的#...#名称一致。目前这里还没设置
        headers = self.replace_data(headers)
        str_data = self.replace_data(str_data)

        # 判断是否存在extractor，存在我们就将数据类型转换成字典
        extractor = {}
        if info['extractor']:
            extractor = json.loads(info['extractor'])


        # 数据类型转换
        headers = json.loads(headers)
        json_data = json.loads(str_data)

        # 2、调用接口得到实际结果
        actual = requests.request(method=method,url=url,headers=headers,json=json_data).json()



        # 调用接口后需要获取投资人、借款人、管理员的id，和token等，设置成类属性，以便我们后面的非登录接口使用比如说：
        # 添加项目要用借款人的id、tokn
        # 审核项目要用管理员的token，还要用添加项目的项目id
        # 投资接口要用投资人的id和审核通过项目的id，和投资人的token
        # 这些数据都需要我们在接口调用后获取到，存储到类的属性中
        # 使用jsonpath进行前面说的接口返回的数据提取供后面使用：在excel中的extractor编写jsonpath表达式
        # extractor中，属性名称为key，jsonpath表达式为value
        # 3、使用for循环extractor和setattr就可以设置类属性了
        for prop_name,jsonpath_expression in extractor.items():
            value = jsonpath(actual,jsonpath_expression)[0]

            # 设置API_Case属性为类属性，这样其他类就可以使用
            setattr(API_Case,prop_name,value)



        # 4、实际结果和预期结果的断言
        for key,value in expected.items():
            self.assertEqual(value,actual[key])