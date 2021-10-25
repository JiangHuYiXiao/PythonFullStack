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
from API接口测试.day4.api接口框架.common.AT_loguru import my_log


# 获取测试数据
register_data= read_excel(file=config.testdata_file,sheetname='register')

@ddt
class Test_Register_API(unittest.TestCase):
    @data(*register_data)
    def test_register(self,i):
        # i就是我们的响应结果数据结果
        '''
        测试注册时手机号为空、格式不对
        :return:
        '''
        case_id = i['case_id']
        title = i['title']
        my_log.info(f'正在执行用例id为：{case_id}，标题为：{title}的自动化测试用例')

        method = i['method']
        # 数据类型转换，因为请求体和请求头都是需要json格式进行数据传输
        headers = json.loads(i['headers'])
        json_data = json.loads(i['json_data'])

        # 因为我们的实际结果经过调用后，返回的结果数据类型为字典，所以对预期结果也需要进行反序列化操作转换成字典
        expected = json.loads(i['expected'])

        # ip地址域名参数化，在config.py中配置域名地址
        register_url = config.host + i['url']

        #调用注册接口得到实际结果
        response = requests.request(method=method, url=register_url, headers=headers,json=json_data)
        actual = response.json()

        #实际结果和预期结果进行断言
        self.assertEqual(expected,actual)

        # 返回值
        return response.json()



