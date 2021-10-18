# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/18 8:42
# @Software       : PythonFullStack
# @Python_verison : 3.7

import requests
# 1，面试题：session 、token 和 cookie 有什么区别？

    # 1、无状态
    # 说到session和token的区别，我们首先需要了解到http协议，http协议有个很重要的特点就是无状态。
    # 何为无状态？就是客户端访向服务端请求第一次后第二次再访问这个地址时，服务端是不知道之前有没有发送过这个请求，
    # 因此客户端每次的请求都是独立的。这样就会造成一个问题，客户端每次必须重新登录才可以操作，每次请求都要发送用户名密码，
    # 这样存在很大的安全问题，也占用带宽。

    # 2、session&cookie
    # 所以才会有session的出现，session就是把用户信息存到服务端，这样每次请求时不用每次都传用户名和密码。
    # 用户访问时，服务端把用户信息保存，并且给客户端返回一个sessionid存储用户数据信息，sessionid就是表明是哪个用户，
    # 每次请求时服务端通过cookie的形式把sessionid返回给客户端，每次客户端访问时，又带上这个存储了sessionid的cookie，和服务端上的校验是否一致。
    # 但是session保存用户信息到服务端也存在几个问题：
    # 用户信息存在服务端会很占用服务器内存。   （使用数据库解决，redis，）
    # 每次都要查询        （然后数据库的压力在再使用数据库集群）
    # session需要和cookie搭配 但是cookie是无法跨域的     （数据库集群）

    # 3、token
    # 就是在客户端存储用户信息，服务端不存储，客户端存储用户信息时不仅存储用户信息还需要存储一个签名信息（唯一标识，经过加密算法得出来的）。
    # 用户信息+签名（sign）= token
    # token可以存在cookie，以及head，indexdb，local storage
    # token相比于session比跨域是方便的
    # token有个问题就是不能注销,如果要删除还是要在服务器中记录，又回到了session的情况。

    # 4、cookie
    # cookie只是session、token的一种表现形式，cookie是http协议请求头字段



# 2， 通过 requests 库，访问 http:www.baidu.com ， 答应响应结果。

res = requests.get('https://www.baidu.com/')
print(res)    # 返回一个对象<Response [200]>

print(res.text)             #  返回一个字符串的数据类型，存储网页信息
print(res.content)             # 返回一个byte数据类型，存储网页信息
# print(res.json())               # 返回一个字典的数据类型，存储的网页信息
print(res.status_code)              # 200