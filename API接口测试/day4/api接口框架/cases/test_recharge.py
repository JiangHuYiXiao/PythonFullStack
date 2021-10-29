# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/28 17:02
# @Software       : PythonFullStack
# @Python_verison : 3.7

'''
注册接口调用步骤：
1、先调用登录接口获取token和member_id
2、将token，X-Lemonban-Media-Type添加到请求头headers中
3、将member_id添加到请求体中
4、调用充值接口recharge
5、校验充值的结果是否正确
'''
import requests
import unittest
from ddt import ddt,data
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import json
from API接口测试.day4.api接口框架.config import user_info
from API接口测试.day4.api接口框架.common.generate_mobile import generate_cell


# 调用登录接口获取token和请求体数据
# {"mobile_phone": "15100002222", "pwd": "12345678"}
recharge_data = read_excel(file=config.testdata_file, sheetname='recharge')
# print(recharge_data)
@ddt
class Recharge_Test(unittest.TestCase):
    @data(*recharge_data)
    def test_recharge(self,i):
        # print('88888888888888888888888888')
        # pwd = "12345678"
        login_headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        # login_body = {"mobile_phone": "15100002222", "pwd": "12345678"}
        login_body = user_info.user
        # login_data = read_excel(file=config.testdata_file,sheetname='login')
        # url = login_data
        login_url = 'http://api.lemonban.com:8766/futureloan/member/login'
        login_response = requests.request(method='post', url=login_url, headers=login_headers, json=login_body).json()
        member_id = str(login_response['data']['id'])
        login_token = login_response['data']['token_info']['token']
        print(login_token)
        # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

        # member_id = "15100002222"
        # 通过DDT获取表格中的数据，str类型
        case_id = i['case_id']
        interface = i['interface']
        title =i['title']
        method = i['method']
        recharge_url = config.host+i['url']
        str_data = i['json']
        str_headers = i['headers']
        # headers = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization":f"Bearer {login_token}"}

        expected = json.loads(i['expected'])
        # 动态参数获取
        # 判断表格中的json是否"#member_id#",存在的话，用登录接口的member_id进行替换
        if "#member_id#" in str_data:
            str_data = str_data.replace("#member_id#",member_id)
        if "#token#" in str_headers:
            str_headers = str_headers.replace("#token#",login_token)
        json_headers = json.loads(str_headers)
        json_data = json.loads(str_data)
        actual = requests.request(method=method,url=recharge_url,headers=json_headers,json=json_data).json()

        # 部分断言
        for key,value in expected.items():
            self.assertEqual(value,actual[key])
        return actual

