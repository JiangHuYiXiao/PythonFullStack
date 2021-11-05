# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/1 12:32
# @Software       : PythonFullStack
# @Python_verison : 3.7


import requests
from jsonpath import jsonpath
from API接口测试.day4.api接口框架.config import user_info, config
import json

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

    def audit_project(self):
        '''
        审核项目
        :return:
        '''
        pass


# print(user_info.user['pwd'])