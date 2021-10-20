# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/19 20:00
# @Software       : PythonFullStack
# @Python_verison : 3.7
import requests
# http请求中我们发送参数时有这几种方式




# 1、请求头中发送，增加参数
url = 'http://httpbin.org/get'
headers = {'a':'aaaa','bala':'balabala'}
response = requests.request(url=url,method='GET',headers = headers)
print(response.text)

# "headers": {
#     "A": "aaaa",
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Bala": "balabala",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-616faeda-1a7de9b005d16d142337e94d"
#   },



# 2、url中传递参数   关键字参数params进行传递
# 我们在postman中，如果需要在请求中添加参数是使用?表示后面为参数，使用&表示多个参数，key=value1&key2=value2
# 但是在requests中是这样表示的
url = 'http://httpbin.org/get'
params = {"a":"aaa"}
response = requests.request(url=url,method='GET',params = params)
print(response.text)

# "args": {
#     "a": "aaa"
# },



# 3、请求体发送参数
    # 3.1 content-type:form-data   使用data关键字参数进行传递

url = 'http://httpbin.org/post'
data = {"a":"aaa","b":"bbbb"}
response = requests.request(url=url,method='POST',data = data)
print(response.text)

# "form": {
#     "a": "aaa",
#     "b": "bbbb"
#   }
# "Content-Type": "application/x-www-form-urlencoded",会自动将content-type修改




    # 3.2 content-type:application/json   使用json关键字参数进行传递
url = 'http://httpbin.org/post'
data = {"a":"aaa","b":"bbbb"}
response = requests.request(url=url,method='POST',json = data)
print(response.text)
# "Content-Type": "application/json",会自动将content-type修改



# *************************************************************************************
# 4、请求头、请求体、url中可以同时传递不同的参数，但是不能同时在请求体中的使用form-data和json
# *************************************************************************************

