# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 17:12
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、什么是接口
# 客户端和服务端通过接口进行数据传输

# 2、接口测试
# 使用工具测试调用api后，的预期结果和实际结果是否一致

# 3、http协议      我们测试接口的大部分协议是http协议
# http请求方法有post、get、delete、options、put、patch
# http请求组成：
# https://ke.qq.com:8080/webcourse/255032/103761876?key=value1&key2=value2#taid=11425901497803832&vid=8602268010484653475
    # https：表示https协议
    # ke.qq.com ：表示域名、ip
    # 8080:表示请求端口
    # /webcourse/255032/103761876 ：请求路径
    # key=value1&key2=value2:   请求参数
    # taid=11425901497803832&vid=8602268010484653475  ：锚点  一种页面内的超级链接


    # post请求和get请求区别：
        # get获取资源               post创建资源
        # get无请求体               post有请求体
        # get可以缓存               post一般不缓存
        # get可以记录历史记录和标签               post不可以记录历史记录和标签

    # get参数传递post参数传递的区别
        # get可以通过url、请求头传递，不能通过请求体
        # post可以通过url、请求头、请求体传递

    # 请求体中参数传递的数据格式content-type    postman会帮我们自动转换数据格式，但是其他工具需要自己填写
        # json     content-type：application/json
        # form表单    content-type：multipart/form-data

