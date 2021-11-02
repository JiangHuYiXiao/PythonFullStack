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
充值接口封装步骤：
1、因为充值时候需要先登录，然后比如后面的取现接口也是需要先登录，这说明登录这个操作是多个地方会重复使用，且是一个前置条件setUp。所以我们可以对登录代码进行封装
2、那么应该封装成函数还是类呢？
    3、封装成函数的话，我们需要调用函数，然后函数必须有返回值，假设其他类比如取现、添加项目、审核项目都需要用，我们都要单独去调用函数
    4、封装成类的话，其他类要用的话我们可以继承登录这个类，然后我们其他类可以使用登录这个类的方法、属性、这个类我们不仅可以封装登录的，还可以封装添加项目、审核项目的操作
    
5、应该封装成login(self)实例方法还是类方法@classmethod呢？
    6、封装成实例方法的话，其他类使用必须使用对象进行调用，但是如果封装成类方法我们其他类可以使用对象或者类都可以调用

7、登录这个方法，我们是应该设置成setUp()还是setUpClass()方法呢，因为我们不是每次充值都需要登录一次，而是登录一次后，可以进行多次充值
所以应该使用etUpClass

8、封装登录的这个类，我们可以把文件放在任何文件夹下，但是通常建议放在cases或者common中
我放common中

'''

import requests
import unittest
from ddt import ddt,data
from API接口测试.day4.api接口框架.common.read_excel import read_excel
from API接口测试.day4.api接口框架.config import config
import json
from API接口测试.day4.api接口框架.common.API_Case import API_Case



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
        actual = requests.request(method=method,url=recharge_url,headers=json_headers,json=json_data).json()

        # 部分断言
        for key,value in expected.items():
            self.assertEqual(value,actual[key])




