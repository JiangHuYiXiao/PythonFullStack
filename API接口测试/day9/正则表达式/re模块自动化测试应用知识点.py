# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/6 12:47
# @Software       : PythonFullStack
# @Python_verison : 3.7

import re
# 就是我们在excel中的那些# #数据
str_token= '{"X-Lemonban-Media-Type":"lemonban.v3", "Authorization": "Bearer #loan_token#"}'
json_data= '{"mobile_phone": "#loan_phone#", "pwd": "#loan_pwd#"}'

result_token1 =  re.search('.*',string=str_token)
print(result_token1)            # <re.Match object; span=(0, 79), match='{"X-Lemonban-Media-Type":"lemonban.v3", "Authoriz>
result_token2 =  re.search('#.*#',string=str_token)
result_token3 =  re.search('#.*?#',string=str_token)
print(result_token2)            # <re.Match object; span=(65, 77), match='#loan_token#'>
print(result_token3)            # <re.Match object; span=(65, 77), match='#loan_token#'>

result_data1 = re.search('.*',json_data)
print(result_data1)         # <re.Match object; span=(0, 53), match='{"mobile_phone": "#loan_phone#", "pwd": "#loan_pw>

result_data2 = re.search('#.*#',json_data)
print(result_data2)         # <re.Match object; span=(18, 51), match='#loan_phone#", "pwd": "#loan_pwd#'>第一个#和第四个#作为开始结束

# 推荐使用这个
result_data3 = re.search('#.*?#',json_data)   # 非贪婪模式，少匹配'#loan_phone#",第一个#和第二#作为开始结束
print(result_data3)         # <re.Match object; span=(18, 30), match='#loan_phone#'>




# 分组()

result_data3 = re.search('#(.*?)#',json_data)   # 非贪婪模式，少匹配'#loan_phone#",第一个#和第二#作为开始结束
print(result_data3)         # <re.Match object; span=(18, 30), match='#loan_phone#'>
print(result_data3.group())         # #loan_phone#
print(result_data3.group(1))         # loan_phone
print(result_data3.group(2))         # IndexError: no such group




