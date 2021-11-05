# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/5 11:08
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、审核项目流程
    # 普通用户登录
    # 添加项目
    # 管理员登录
    # 审核项目

# 2、测试类编写步骤
    # 准备测试数据
    # 调用审核项目接口
    # 断言对预期结果和实际结果

import unittest
import json
from ddt import ddt,data
from API接口测试.day4.api接口框架.common.API_Case import API_Case
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import requests
audit_data = read_excel(file=config.testdata_file,sheetname='audit')
@ddt
class Test_Audit_Project(unittest.TestCase,API_Case):
    @classmethod
    def setUpClass(cls):
        # 普通用户登录
        cls.login()
        # 管理员用户登录
        cls.admin_login()

    def setUp(self):
        '''每个测试用例都需要重新添加项目，如果写在setUpClass中则一个类只能用一个，然后第二个用例就不能再次创建项目了'''
        self.add_project(self.member_id,self.login_token)

    def tearDown(self):
        pass

    @data(*audit_data)
    def test_audit_project(self,info):
        # 从excel中获取测试用例数据
        case_id = info['case_id']
        interface = info['interface']
        method = info['method']
        title = info['title']
        url = config.host+ info['url']
        str_headers = info['headers']
        str_data = info['json']
        expected = json.loads(info['expected'])
        if "#admin_token#" in str_headers:
            str_headers = str_headers.replace("#admin_token#",self.admin_login_token)

        if "#loan_id#" in str_data:
            str_data = str_data.replace("#loan_id#",self.loan_id)

        # 将str_data，str_headers转换成json格式
        headers= json.loads(str_headers)
        json_data = json.loads(str_data)
        audit_response = requests.request(method=method,url=url,headers=headers,json=json_data).json()

        # 部分断言
        for key,value in expected.items():
            self.assertEqual(value,audit_response[key])
