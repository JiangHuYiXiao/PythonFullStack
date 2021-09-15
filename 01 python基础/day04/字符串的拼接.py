# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 15:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

'''
字符串的拼接方法很多，在这归纳总结下各种方式的特点：
join()：使用特定的拼接符将列表进行拼接，返回一个字符串，并且需要事先有一个列表。
+    ：比较繁琐。
f-string  :比较灵活，尤其是一些复杂格式的拼接时。
'''

# 1、*************+****************
print('a'+'b')
info = '''
姓名：
年龄：
身高：
'''
print('姓名：'+'jianghu'+'年龄：'+str(19)+'身高：'+'170')            # 姓名：jianghu年龄：19身高：170
print('姓名：'+'jianghu'+'\n'+'年龄：'+str(19)+'\n'+'身高：'+'170')
# 姓名：jianghu
# 年龄：19
# 身高：170


# 2、**************join([age,name,height])**************
res = '_'.join(['age','name','height'])
print(res)


# 3、**************f-string************
# '''
# 姓名：
# 年龄：
# 身高：
# '''
name = 'jianghu'
age = 19
height = 190
info = f'''
姓名：{name}
年龄：{age}
身高：{height}
'''
print(info)
# 姓名：jianghu
# 年龄：19
# 身高：190

# 4、***************format()****************
name = 'jianghu'
age = 19
height = 190

print('''
姓名：{name}
年龄：{age}
身高：{height}
'''.format(name=name, age=age, height=height))

print('''
姓名：{}
年龄：{}
身高：{}
'''.format(1111, 6666, 6666))
# 姓名：1111
# 年龄：6666
# 身高：6666