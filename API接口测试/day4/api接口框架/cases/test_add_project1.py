# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/4 16:10
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 添加项目业务流程
    # 1、普通用户登录
    # 2、添加项目


# 测试类编写步骤
    # 1、准备测试数据json_data,headers,expected等
    # 2、调用接口得到实际结果
    # 3、预期结果和实际结果的断言


import unittest
import requests
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from ddt import ddt,data
from API接口测试.day4.api接口框架.config import config
from API接口测试.day4.api接口框架.config.user_info import user
from API接口测试.day4.api接口框架.common.API_Case import API_Case
add_project_data = read_excel(file=config.testdata_file,sheetname="add")
import json
@ddt
class Test_Add_Project(unittest.TestCase,API_Case):
    # 调用API_case 获取登录的login_token和member_id
    @classmethod
    def setUpClass(cls):
        cls.login()



    @data(*add_project_data)
    def test_add_pro(self,info):
        # 准备测试数据
        case_id = info['case_id']
        interface = info['interface']
        title = info['title']
        method = info['method']
        url = config.host + info['url']
        str_data = info['json']
        str_headers = info['headers']
        expected = json.loads(info['expected'])

        # 判断excel中是否有未知的数据或者有变化的数据有用# #标记的，我们一般对运行时不知道或者有变化的数据用# #标记

        if "#member_id#" in str_data:
            str_data = str_data.replace("#member_id#",self.member_id)

        if "#token#" in str_headers:
            str_headers = str_headers.replace("#token#",self.login_token)

        headers = json.loads(str_headers)
        json_data = json.loads(str_data)
        # 调用添加项目接口
        add_project_response = requests.request(method=method,url=url,headers=headers,json=json_data).json()

        # 部分断言
        for key,value in expected.items():

            self.assertEqual(value,add_project_response[key])









