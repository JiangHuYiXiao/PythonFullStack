# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/4 9:14
# @Software       : PythonFullStack
# @Python_verison : 3.7


# 1、添加项目接口的调用流程

# 1.1、接口地址http://api.lemonban.com:8766/futureloan/loan/add
# 1.2、请求头headers中添加：
    # 请求方式：post
    # 固定参数：X-Lemonban-Media-Type：lemonban.v2
    # 数据格式：Content-Type：application/json   可以不添加因为我们后面请求体中用的是json会默认帮我们转换成json格式
    # 调用登录接口获取普通用户的登录的token：Authorization：Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjgzLCJleHAiOjE2MzU5ODk2MDd9.fOCBrEzgrQ1kYfVh-dQnmhX4oyziY1d5KxslRK8mHybW5BFesnbGYbjjjxCWQJYE7JOyZeW4jwlfIKLJAcdw_w
# 1.3、请求体body中添加数据json=：
    # { "member_id":83, "title":"报名 Java 全栈自动化课程", "amount":600.00, "loan_rate":12.0, "loan_term":12, "loan_date_type":1, "bidding_days":5 }
# 1.4 、调用添加项目接口



# 2、审核项目
# 首先需要添加项目
# 2.1、接口地址：http://api.lemonban.com:8766/futureloan/loan/audit
# 2.2、管理员用户登录，获取到管理员的登录token
# 2.3、请求头headers中添加：
    # 请求方式：post
    # 固定参数：X-Lemonban-Media-Type：lemonban.v2
    # 数据格式：Content-Type：application/json   可以不添加因为我们后面请求体中用的是json会默认帮我们转换成json格式
    # 调用登录接口获取管理员用户的登录的token：
# 2.4、请求体中body中添加数据json=
# { "loan_id":777, "approved_or_not":true}
