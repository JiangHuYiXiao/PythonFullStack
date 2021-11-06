# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/6 10:38
# @Software       : PythonFullStack
# @Python_verison : 3.7


# 正则表达式：就是一个字符串数据提取的一个表达式，字符串模糊匹配的一个技术。
# 只要在字符串中查找数据，就都可以用正则表达式。
# **********************注意正则表达式匹配的是连着的一段子字符串******************
# 在python中使用的是re模块

import re


string = 'jianghuyixiao'

# 1、简单的，使用要获取的字符串作为表达式
result = re.search('a',string=string)

# 使用group()获取到匹配字符串的子字符串
result.group()
print(result)               # <re.Match object; span=(2, 3), match='a'>   span表示索引位置，match表示匹配的结果



# 2、元字符'.'匹配任意一个字符,除了\n
result = re.search('.',string=string)
result.group()
print(result)               # <re.Match object; span=(0, 1), match='j'>

# 3、[7a]表示匹配中括号中的数据，表示可以匹配7或者a,哪个先出现匹配哪个

string1 = 'fffaa777'
result1 = re.search('[7a]',string=string1)
print(result1.group())   # a


# 4、匹配数字
string2 = 'fffaa777'
result2 = re.search('\d',string=string1)
print(result2.group())          # 7



# 5、表示数字
# * 表示匹配前一个字符零次或者多次，默认是多次，因为python中的正则表达式默认是贪婪模式

string3 = 'jianghuyixiaohu'
result3 = re.search('j*',string=string3)
print(result3.group())      # j
result3 = re.search('a*',string=string3)
print(result3.group())    # 空

# 6、匹配字符串的所有：'.*?'在我们自动化测试中用的最多
string4 = 'jianghuyixiaohu'
result4 = re.search('.*',string=string4)
print(result4)              # <re.Match object; span=(0, 15), match='jianghuyixiaohu'>

print(result4.group())              # jianghuyixiaohu


# 贪婪模式vs非贪婪模式
# python中默认正则表达式为贪婪模式
# 非贪婪模式 需要在正则表达式后面加上?问号

string4 = 'jianghuyixiaohu'
result4 = re.search('.*?',string=string4)
print(result4)              # <re.Match object; span=(0, 0), match=''>