# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/1 10:57
# @Software       : PythonFullStack
# @Python_verison : 3.7


'''
充值接口调用步骤：
1、先调用登录接口获取token和member_id
2、将token，X-Lemonban-Media-Type添加到请求头headers中
3、将member_id添加到请求体中
4、调用充值接口recharge
5、校验充值的结果是否正确
'''


'''
充值接口余额校验使用数据库

'''

import requests
import unittest
from ddt import ddt,data
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import json
from API接口测试.day4.api接口框架.common.API_Case import API_Case
from API接口测试.day4.api接口框架.common.db_handler import DBHandler
from decimal import Decimal

# 调用登录接口获取token和请求体数据

recharge_data = read_excel(file=config.testdata_file, sheetname='recharge')

@ddt
class Recharge_Test(unittest.TestCase,API_Case):

    # def setUp(self):   # 这样封装的话，我们每个用例都会执行登录，实际其实我们在这个类中只需要登录一次就行了

        # 调用API_Case中封装的login方法获取member_id，和login_token

        # 方式1
        # 使用类调用login方法,根据返回值获取
        # self.member_id,self.login_token = API_Case.login()

        # 方式2
        # 使用类调用login方法中的属性，因为是一个类方法
        # API_Case.login()
        # self.member_id = API_Case.member_id
        # self.loign_token = API_Case.login_token

        # 方式3
        # Recharge_Test直接继承API_Case,那么，member_id和login_token就可以直接使用
        # self.login()

    @classmethod
    def setUpClass(cls):        # 这样封装的话，我们这个类中只需要登录一次后面用例就可以使用登录了

        cls.login()             # 可以使用cls，因为类可以调用API_Case中的属性和方法
    def setUp(self):
        '''连接数据库'''
        self.db = DBHandler()


    def tearDown(self):
        '''关闭数据库'''
        self.db.close()

    @data(*recharge_data)
    def test_recharge(self,i):
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
            str_data = str_data.replace("#member_id#",self.member_id)
        if "#token#" in str_headers:
            str_headers = str_headers.replace("#token#",self.login_token)
        json_headers = json.loads(str_headers)
        json_data = json.loads(str_data)
        amount = json_data["amount"]


        # 获取充值前的结果
        sql = f'select leave_amount from member where id={self.member_id};'
        before_money = self.db.query_one(sql)[0]  # 返回值是一个tuple所以需要加索引,而且还是一个decimal，所以需要导入decima

        actual = requests.request(method=method,url=recharge_url,headers=json_headers,json=json_data).json()

        # 部分断言
        for key,value in expected.items():
            self.assertEqual(value,actual[key])

        # 对于余额校验，我们可以有几种办法
        # 方法1：
            # 使用接口进行校验，充值前进行登录后，登录接口会返回余额
            # 然后我们再调用充值接口，会返回一个余额，那么这两个余额相差就是充值的多少
            # 但是这样需要把登录login设置为setUp，而不是设置为setUpClasss
        # 方法2
            # 查询数据库，充值后
            # 只有充值成功的我们才需要校验余额，通过msg进行判断下
        # 方法3
            # 调用两次充值接口
            # 两次结果作比较就可以知道充值是否成功

        # 我们使用数据库校验的方式
        # 充值后的结果
        if actual['msg'] == "OK":
            sql = f'select leave_amount from member where id={self.member_id};'
            after_money = self.db.query_one(sql)[0]  # 返回值是一个tuple所以需要加索引,
            # 而且还是一个decimal，所以需要导入decimal,处理我们的充值的值，因为充值的值可能是小数或者整数，且Decimal需要的数据类型是str

            self.assertEqual(after_money - before_money,Decimal(str(amount)))


