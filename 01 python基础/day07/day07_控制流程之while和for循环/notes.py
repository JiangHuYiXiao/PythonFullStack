# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/8 8:58
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、 while 循环结构：
#     while 判定条件：
#         改变条件语句

# 2、while True：
#     死循环


# 3、for 循环结构：
# for 条件：
#     循环体

# enumumrate 同时获取索引和key
for key,value in enumerate({'a':1,'b':2}):
    print(key,value)    # 结果字典的索引，和key
    # 0 a
    # 1 b

for key,value in {'a':1,'b':2}.items():
    print(key,value)    # 字典的索引和值一般这样获取

for key,value in enumerate([1,2,'balala']):
    print(key,value)   # 结果为列表的索引和值
# 0 1
# 1 2
# 2 balala

# 4、break和continue
# break终止整个循环
# continue终止当前循环，然后执行下一次循环

# 5、range
# 返回整数0-9
print(range(10))
for i in range(10):
    print(i)

# 6、print
print(end='\t') # 表示一行输出，默认是换行的\

# 7、格式化输出
# 格式化输出的另一种使用方式：f
a = 'jianghu'
b = 19
print(f'我的名字是{a}，我的年龄是{b}岁')

# 8、转义符
# 取消转义符 r
print(r'ab\n')
print('ab\n123213123')
