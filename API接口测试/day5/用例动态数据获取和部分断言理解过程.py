# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/27 15:54
# @Software       : PythonFullStack
# @Python_verison : 3.7


from API接口测试.day4.api接口框架.common.generate_mobile import generate_cell

# 动态参数获取，通过if 判断#mobile_phone#是否存在预期结果中
# 通过faker第三方模块生成手机号，这样注册接口中的每次用的就是不一样的手机号

str_data = '{"mobile_phone":"#mobile_phone#","pwd":"12345678"}'
if "#mobile_phone#" in str_data:
    print('mobile_phone存在表格中')
    mobile = generate_cell()
    res = str_data.replace("#mobile_phone#",mobile)
    print(res)
    print(str_data)


# 部分断言
# 因为我们之前写的用例断言都是全量断言，如果存在很多数据这样断言耗费太大，而且不一定准确，有的数据都是动态的比如id
expected = {
    "code": 2,
    "msg": "无效的手机格式"}

actual = {
    "code": 2,
    "msg": "无效的手机格式",
    "data": None,
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}
for key, value in expected.items():
    print(value,actual[key])
