# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/28 10:38
# @Software       : PythonFullStack
# @Python_verison : 3.7


import requests
import unittest
from ddt import ddt,data
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import json
from API接口测试.day4.api接口框架.common.generate_mobile import generate_cell
from API接口测试.day4.api接口框架.config.user_info import user



login_data = read_excel(file=config.testdata_file,sheetname='login')

@ddt
class Login_Test(unittest.TestCase):
    '''
    注册接口调用步骤：
    1、先调用登录接口获取token和member_id
    2、将token，X-Lemonban-Media-Type添加到请求头headers中
    3、将member_id添加到请求体中
    4、调用充值接口recharge
    5、校验充值的结果是否正确
    '''
    @data(*login_data)
    def test_login(self,i):
        '''

        :return:
        '''
        method = i['method']
        case_id = i['case_id']
        title = i['title']
        interface = i['interface']
        url = config.host + i['url']
        str_data = i['json']
        # 将字符串转换成json格式

        headers = json.loads(i['headers'])
        expected = json.loads(i['expected'])


        # 1、调用登录接口
            # 判断一个新的虚拟的手机号是否可以登录，
        if "#new_phone#" in str_data:
            mobile = generate_cell()
            str_data = str_data.replace("#new_phone#",mobile)


            # 判断#investor_phone#是否存在excel中的表格中
            # 并且判断"#investor_pwd#"是否存在excel表格中
        if '#investor_phone#' in str_data:
            str_data = str_data.replace("#investor_phone#",user['mobile_phone'])
            if "#investor_pwd#" in str_data:
                str_data= str_data.replace("#investor_pwd#",user['pwd'])

        # 将str_data转成json_data
        json_data = json.loads(str_data)

        login_response = requests.request(method=method,url=url,headers=headers,json=json_data)
        actual = login_response.json()

        # 部分断言
        for key,value in expected.items():

            self.assertEqual(value,actual[key])