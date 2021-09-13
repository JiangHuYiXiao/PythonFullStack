# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 18:56
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 转义
# \n  换行
# \t  水平制表符
# r  关闭转义

hi = 'hello\nworld'
print(hi)
# hello
# world

hi = 'hello\tworld'
print(hi)    # hello	world

hi = r'hello\nworld'
print(hi)    # hello\nworld


str1 = 'jiang hu yi xiao'

# 1、split()拆分、切割成一个列表
print(str1.split(' '))          # ['jiang', 'hu', 'yi', 'xiao']

str2 = 'jiang#hu#yi xiao'
print(str2.split('#'))

# 2、join()  将列表拼接成字符串
list1 = ['天猫双','11','购物节']
res = ''.join(list1)
print(res)  # 天猫双11购物节

res = '@'.join(list1)
print(res)  # 天猫双@11@购物节

# 3、find  返回找到的该子字符的索引，多个就返回第一个，找不到则返回-1

str_j = 'jianghuxixiao'
print(str_j.find('a'))              # 2
print(str_j.find('ang'))          # 2
print(str_j.find('ag'))          # -1 必须同时在一起
print(str_j.find('ang11'))          # -1

# 4、index  返回找到的字符串，和find的作用是一样的，但是index找不到报错
str_j = 'jianghuxixiao'
# print(str_j.index('dfsafd'))            # ValueError: substring not found


# 5、replace()  替换某个子字符串,返回一个新的字符串，源字符串没有改变
str = 'so hu obj'
print(str.replace('o', 'hh'))               # shh hu hhbj
print(str)              # 原字符串不变

# 6、upper()返回一个所有字符都大写的字符串,原字符串不变，新生成一个
print(str.upper())          # SO HU OBJ
print(str)          # so hu obj

# 7、lower()返回一个所有字符都小写的字符串,原字符串不变，新生成一个
print('HELLO'.lower())              # hello



# 8、字符串的格式化操作

# f_string,python3.6之后用这种格式，之前是用的format
name ='jianghu'
jie_name = 'yixiu'
time = '2021-12-31'
money = '200万'

info = f'''
借条:
今天{name}借了{jie_name},
{money}元,按照约定{time}归还
署名:{name}
'''
print(info)

# '''借条:
# 今天jianghu借了yixiu,
# 200万元,按照约定2021-12-31归还
# 署名:jianghu'''
# '''

# 使用format进行字符串的格式化
info = '''
借条:
今天{name1}借了{jie_name1},
{money1}元,按照约定{time1}归还
署名:{name1}
'''
# print(info.format('江湖','yutong',1222,'2021-12-31','江湖'))
# '''借条:
# 今天江湖借了yutong,
# 1222元,按照约定2021-12-31归还
# 署名:江湖
# '''

print(info.format(name1='江湖',jie_name1='yutong',money1=1222,time1='2021-12-31'))

# 借条:
# 今天江湖借了yutong,
# 1222元,按照约定2021-12-31归还
# 署名:江湖


# 字符串格式化操作的自动化测试场景，接口地址的拼接
host = 'http://127.0.0.1:8080'
interface = 'getlist?'
params = 'data=100&page=2'
interface_address = f'{host}{interface}{params}'
print(interface_address)