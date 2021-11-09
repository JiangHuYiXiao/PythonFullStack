# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/1 12:32
# @Software       : PythonFullStack
# @Python_verison : 3.7


import requests
from jsonpath import jsonpath
from API接口测试.day4.api接口框架.config import user_info, config
import json
import re

class API_Case:
    @classmethod
    def login(cls):
        '''
        前程贷登录操作,因为登录只需要调用一次，且使用类方法可以使用类调用方法或者属性，也可以使用对象调用类方法和属性
        :return: self.member_id,self.login_token
        '''
        login_headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        login_body = user_info.user
        login_url = 'http://api.lemonban.com:8766/futureloan/member/login'
        login_response = requests.request(method='post', url=login_url, headers=login_headers, json=login_body).json()
        # print(login_response)
        # 获取member_id,使用字典方式
        # self.member_id = str(login_response['data']['id'])

        # 获取member_id,使用jsonpath方式
        cls.member_id = str(jsonpath(login_response,'$..id')[0])

        # 获取登录的token，使用字典的方式
        # login_token = login_response['data']['token_info']['token']

        # 获取登录的token,使用jsonpath方式
        cls.login_token = jsonpath(login_response,'$..token')[0]

        # cls.login_pwd = user_info.user['pwd']

        return (cls.member_id,cls.login_token)          # 如果封装成类方法，这个返回值我们都可以去掉

    @classmethod
    def admin_login(cls):
        '''
        前程贷登录操作,因为登录只需要调用一次，且使用类方法可以使用类调用方法或者属性，也可以使用对象调用类方法和属性
        :return: self.member_id,self.login_token
        '''
        login_headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        login_body = user_info.admin_user
        login_url = 'http://api.lemonban.com:8766/futureloan/member/login'
        login_response = requests.request(method='post', url=login_url, headers=login_headers, json=login_body).json()
        # print(login_response)
        # 获取member_id,使用字典方式
        # self.member_id = str(login_response['data']['id'])

        # 获取member_id,使用jsonpath方式
        cls.admin_member_id = str(jsonpath(login_response, '$..id')[0])

        # 获取登录的token，使用字典的方式
        # login_token = login_response['data']['token_info']['token']

        # 获取登录的token,使用jsonpath方式
        cls.admin_login_token = jsonpath(login_response, '$..token')[0]

        # cls.login_pwd = user_info.user['pwd']

        return (cls.admin_member_id, cls.admin_login_token)  # 如果封装成类方法，这个返回值我们都可以去掉



    @classmethod
    def add_project(cls, member_id,login_token):
        '''
        封装添加项目的方法
        :param member_id:
        :param login_token:
        :return:
        '''
        # 准备测试数据

        # member_id，login_token不传参数的话就需要手动获取，然后再去替换json_data中的# #数据
        # cls.member_id,cls.login_token = cls.login()
        json_data= {"member_id":member_id,"amount":100, "title": "小目标", "loan_rate": 18, "loan_term": 5, "loan_date_type": 1, "bidding_days": 1}
        headers = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization": f"Bearer {login_token}"}
        add_project_url = config.host+'/loan/add'


        # 调用添加项目接口
        add_project_response = requests.request(method='post', url=add_project_url, headers=headers, json=json_data).json()
        cls.loan_id = str(jsonpath(add_project_response,'$..id')[0])

        return add_project_response
    @classmethod
    def audit_project(cls,load_id,admin_login_token):
        '''

        审核项目
        :return:
        '''
        json_data = {"loan_id":load_id, "approved_or_not": True}
        headers = {"X-Lemonban-Media-Type":"lemonban.v2", "Authorization": f"Bearer {admin_login_token}"}
        audit_project_url = config.host+'/loan/audit'

        audit_project_response= requests.request(method='patch',url=audit_project_url,headers=headers,json=json_data).json()
        return audit_project_response



    @classmethod
    def replace_data(cls,string):           # 类方法，那么设置类属性可以写在setUpClass中，用cls去设置属性，或者写在setUp中用API_Case去设置，因为cls和API_Case才表示类本身
        '''
        尽量设置为类方法，这样我们不仅可以使用类调用还可以使用对象调用
        使用正则表达式替换excel中的动态数据
        :param string:
        :return: 替换后的字符串
        '''
        result = re.finditer('#(.*?)#',string)
        for el in result:
            old = el.group()    #                #pwd#
            new = getattr(cls,el.group(1))       # pwd
            string = string.replace(old,str(new))
        return string

    # def replace_data(self,string):          # 实例方法，那么设置实例属性就必须写在setUp中,用self去设置属性，因为self表示的实例本身
    #     '''
    #     使用正则表达式替换excel中的动态数据
    #     :param string:
    #     :return: 替换后的字符串
    #     '''
    #     result = re.finditer('#(.*?)#',string)
    #     for el in result:
    #         old = el.group()    #                #pwd#
    #         new = getattr(self,el.group(1))       # pwd
    #         string = string.replace(old,str(new))
    #     return string


    def pre_data(self,info):
        '''

        :param info:
        :return: 替换后的info
        '''

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

        info['headers'] = headers
        info['json'] = json_data
        info['expected'] = expected
        info['extractor'] = extractor

        return info


    def visit(self,info):
        '''
        访问接口
        :return:
        '''

        actual = requests.request(method=info['method'], url=config.host + info['url'], headers=info['headers'], json=info['json']).json()
        return actual


    # def extractor(self,response,info):
    #     '''
    #     设置属性
    #     :return: None
    #     '''
    #     for prop_name,jsonpath_expression in info['extractor'].items():
    #         value = jsonpath(response,jsonpath_expression)[0]
    #
    #         # 设置API_Case属性为类属性，这样其他类就可以使用
    #         setattr(API_Case,prop_name,value)
    @classmethod
    def extractor(cls,response,info):
        '''
        设置属性
        :return: None
        '''
        for prop_name,jsonpath_expression in info['extractor'].items():
            value = jsonpath(response,jsonpath_expression)[0]

            # 设置API_Case属性为类属性，这样其他类就可以使用
            setattr(cls,prop_name,value)

    def assert_all(self,info,response):
        '''
        断言
        :return: None
        '''
        for key,value in info['expected'].items():
            self.assertEqual(value,response[key])


    def steps(self,info):
        '''把四个函数都封装到steps函数中'''
        # 1、数据预处理
        info = self.pre_data(info)

        # 2、调用接口得到实际结果
        actual = self.visit(info)

        # 3、数据提取
        self.extractor(response=actual,info= info)

        # 4、实际结果和预期结果的断言
        self.assert_all(info=info,response=actual)