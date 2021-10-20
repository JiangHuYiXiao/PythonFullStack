# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/20 14:13
# @Software       : PythonFullStack
# @Python_verison : 3.7

import requests,json
# requests有三种响应格式
# text(str)、content(byte)、json(dict)这就要涉及到各个数据类型格式之间的转换

# json注意点
    # json是字符串数据类型的一个格式
    # json格式的数据类型本质还是str然后里面就是一个字典，然后引号是用的双引号，
    # 为啥要有json，因为json在数据传输更方便，将json使用dumps序列化后可以直接根据键值对的键值就可以取出值。
    # json中的键值都是用双引号，Python对应的None，json中用null，且首字母都是大写
    # json中的布尔值都是小写

url = 'http://httpbin.org/get'
params = {"a":"aaa"}
response = requests.request(url=url,method='GET',params = params)
text_response = response.text
content_response = response.content
dict_response = response.json()

print(text_response,type(text_response))
print(content_response,type(content_response))
print(dict_response,type(dict_response))

# 接口响应结果数据类型转换
    # str ---> byte             编码

byte_response = text_response.encode()
print(byte_response)


    # byte ---> str             解码
str_response = content_response.decode()
print(str_response)


# str ---> json    方式1：序列化，将其他数据类型转换成json格式，方式2：还有eval()去掉引号
dumps_response = json.dumps(text_response)
print(dumps_response,type(dumps_response))              # <class 'str'>
# "{\n  \"args\": {\n    \"a\": \"aaa\"\n  }, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Accept-Encoding\": \"gzip, deflate\", \n    \"Host\": \"httpbin.org\", \n    \"User-Agent\": \"python-requests/2.24.0\", \n    \"X-Amzn-Trace-Id\": \"Root=1-616fbc23-25b29da81c6c173a3cd1431e\"\n  }, \n  \"origin\": \"219.133.170.76\", \n  \"url\": \"http://httpbin.org/get?a=aaa\"\n}\n" <class 'str'>


# json --->str          方式1：反序列化  将json格式转换成其他数据类型  方式2：‘’加上引号就是字符串也可以
json_response = json.loads(dumps_response)          # <class 'str'>
print(json_response,type(json_response))

# {
#   "args": {
#     "a": "aaa"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-616fbd27-2624b9766e18e91c31713603"
#   },
#   "origin": "219.133.170.76",
#   "url": "http://httpbin.org/get?a=aaa"
# }
