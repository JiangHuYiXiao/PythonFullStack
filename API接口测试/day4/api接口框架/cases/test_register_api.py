# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/22 10:32
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 测试用例编写步骤
    # 1、准备测试数据
    # 2、准备预期结果
    # 3、调用测试函数获取实际结果
    # 4、对实际结果和预期结果进行断言

import requests
from ddt import ddt,data
import unittest
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import json


# 获取测试数据
register_data= read_excel(file=config.testdata_file,sheetname='register')
# @ddt
class Test_Register_API(unittest.TestCase):
    # @data(*register_data)
    def test_register_mobile_null(self,i):
        '''
        测试注册时手机号为空
        :return:
        '''

        case_id = json.loads(['case_id'])
        title = json.loads(['title'])
        method = json.loads(['method'])
        headers = json.loads(i['headers'])
        expected = json.loads(i['expected'])
        json_data = json.loads(i['json_data'])
        register_url = 'http://api.lemonban.com:8766/futureloan/member/register'
        response = requests.request(method='POST', url=register_url, headers=headers,json=json_data)
        actual = response.json()
        self.assertEqual(expected,actual)
        print(response.json())



