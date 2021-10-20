# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/20 8:59
# @Software       : PythonFullStack
# @Python_verison : 3.7

import requests

# requests.get()
# requests.post()
# 在源码中这两个方法的内部都是在return时会调用return request('post', url, data=data, json=json, **kwargs)
# 所以我们可以使用request进行请求方法的配置def request(method, url, **kwargs):

# 1、GET
url = 'http://127.0.0.1:8000/api/search_event/?eid=101'
# 方式1：
# response_GET = requests.get(url=url)

# 方式2：推荐使用,这样我们每次请求都不要去判断为何种请求方式，如果使用方式1则需要使用if判断
response_GET = requests.request(method='GET',url=url)

print(response_GET.json())


# 2、POST
# 方式1：
# response_POST = requests.post(url=url)

# 方式2：推荐使用
response_POST = requests.request(method='POST',url=url)


print(response_POST.json())

# 3、PUT
response_PUT= requests.request(method='PUT',url=url)
print(response_PUT)