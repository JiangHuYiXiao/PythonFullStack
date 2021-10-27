# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/27 14:48
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、前面进行注册接口测试的时候，手机号码执行两次就会报错，提示号码已经存在，所以接下来我们需要对这种重复执行的数据进行处理
# 处理方案：
    # 1、手机号+1
    # 2、执行后，删除自己的那条数据
    # 3、随机生成一个手机号码，使用faker第三方模块进行数据伪造


from faker import Faker

# 修改locale为中国的
faker = Faker(locale=['zh-cn'])
# 地址
print(faker.address())
# 姓名
print(faker.name())
# 公司
print(faker.company())
# 手机号
print(faker.phone_number())
# 身份证
print(faker.ssn())
