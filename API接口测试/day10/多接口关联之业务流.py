# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/6 15:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 使用正则表达式获取excel中的动态数据
# 多接口关联
# 方法1：
    # 数据准备：我们可以使用我们之前的方法1这个也是可以处理的，通过read_excel读取excel中的数据，
    # 数据替换：然后用if判断来替换#...#数据，一个#...#需要写一个if判断，这个就是比较麻烦如果#...#较多，数据类型转换将接口需要的headers、json_data转换成字典格式
    # 前置条件：编写setUp，setUpClass，在这个里面调用在API_Case中编写的一些通用的方法，作为接口调用之前的前置条件
    # 调用测试接口：requests.request()
    # 断言

# 方法2：
    # （使用这个方式读取数据的话，我们在excel中需要把每一个步骤用的接口信息和测试数据填上去，然后最好还要有个extractor数据提取）
    # 数据准备：我们可以使用我们之前的方法1这个也是可以处理的，通过read_excel读取excel中的数据，
    # 数据替换：然后用我们在API_Case封装的正则表达式replace_data方法来替换#...#数据，数据类型转换将接口需要的headers、json_data转换成字典格式
    # 前置条件：编写setUp，读取user_info中的登录的用户信息配置数据
    # 调用测试接口：requests.request()
    # 断言