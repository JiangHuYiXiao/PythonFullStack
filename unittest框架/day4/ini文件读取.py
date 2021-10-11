# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/11 10:42
# @Software       : PythonFullStack
# @Python_verison : 3.7

# ini文件只支持字符串，所以用的较少，我们重点关注yaml
from configparser import ConfigParser
parser = ConfigParser()
parser.read('demo.ini',encoding='utf-8')
host = parser.get('default','host')
db_host = parser.get('db','host')
print(host)
print(db_host)