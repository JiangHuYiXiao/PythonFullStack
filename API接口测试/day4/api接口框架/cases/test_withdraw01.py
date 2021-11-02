# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/2 8:56
# @Software       : PythonFullStack
# @Python_verison : 3.7

'''
取现接口测试
    接口地址：http://api.lemonban.com:8766/futureloan/member/withdraw
'''
import unittest
import requests
from API接口测试.day4.api接口框架.common.API_Case import API_Case
from API接口测试.day4.api接口框架.common.db_handler import DBHandler
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
from ddt import ddt,data
import json
from API接口测试.day4.api接口框架.common.AT_loguru import my_log
from decimal import Decimal

# url = "http://api.lemonban.com:8766/futureloan/member/withdraw"
# headers = {"X-Lemonban-Media-Type": "lemonban.v2",
#            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjgzLCJleHAiOjE2MzU4MTU2MjB9.MRR0B8vdd4HdZ08inr6cD7U6gk8BMBLHNe2RMw6gTPz02gz9rQd4mgThFmGR3bthUfOgquGY_ixyuCSUamSR4g"}
# data ={"member_id":"83","amount":1}
# withdraw_response = requests.request(method="post",url=url,headers=headers,json=data)
# print(withdraw_response.json())

withdraw_data = read_excel(file=config.testdata_file, sheetname='withdraw')
@ddt
class Test_Withdraw(unittest.TestCase,API_Case):
    @classmethod
    def setUpClass(cls):
        '''调用API_Case中的登录方法'''
        cls.login()
        my_log.info('执行登录接口成功')
    def setUp(self):
        '''连接数据库'''

        self.DB = DBHandler()
        my_log.info('连接数据库成功')
    def tearDown(self):
        '''关闭数据库连接'''
        self.DB.close()
        my_log.info('关闭数据库成功')

    @data(*withdraw_data)
    def test_withdraw(self,info):
        '''
        1、准备测试数据
        2、调用函数得到实际结果
        3、获取预期结果
        4、对预期结果和实际结果进行断言

        :return:
        '''
        # 通过ddt读取excel中的用例数据
        case_id = info['case_id']
        title = info['title']
        method = info['method']
        url = config.host + info['url']
        str_data = info['json']
        headers = info['headers']
        # 这里直接转换，因为后面对于expected数据不需要进行替换
        expected = json.loads(info['expected'])

        # 判断excel中的json列字段中是否有#member_id#
        if "#member_id#" in str_data:
            str_data = str_data.replace("#member_id#",self.member_id)
        if "#token#" in headers:
            headers = headers.replace("#token#",self.login_token)

        # 将字符串的str_data请求体和headers的请求头转换为json格式
        # 因为我们在调用接口时候，是用来json关键字参数，所以我们不需要指定请求体的content-type
        json_data = json.loads(str_data)
        headers = json.loads(headers)
        # 调用取现接口前查询数据库中的余额
        sql = f'select leave_amount from member where id={self.member_id};'
        # 查询结果为元组，所以要使用索引取值
        before_money = self.DB.query_one(sql)[0]

        # 获取excel中的amount
        amount = json_data['amount']
        # 转换为Decimal
        # Decimal(str(amount))


        # 调用接口,
        withdraw_response = requests.request(method=method,url=url,headers=headers,json=json_data)
        actual = withdraw_response.json()

        # 部分断言
        for key,value in expected.items():
            self.assertEqual(value,actual[key])


        # 取现后余额校验
        if actual['msg'] == "OK":
            sql = f'select leave_amount from member where id={self.member_id};'
            after_money = self.DB.query_one(sql)[0]
            my_log.info(f'取现后的余额为：{after_money}')
            self.assertEqual(before_money-after_money,Decimal(str(amount)))




