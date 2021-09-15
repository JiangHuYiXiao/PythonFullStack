# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/9 15:28
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、三引号表示字符串和注释的区别在于是否用了变量存储数据
q = '''jianghuyixiao'''
'''jianghuyixiao'''

# 2、字符串的索引操作
# 索引从0开始

str1 = 'jianghuyixiao'

# 获取第一个字符
print(str1[0])
# 获取第一个索引
print(str1[1])

# 索引可以为负数
print(str1[-1])
print(str1[-2:])   # 取后两位数据ao

# 索引越界
# print(str1[90])   # IndexError: string index out of range  超过最大长度会报索引越界
# print(str1[13])   # IndexError: string index out of range  超过最大长度会报索引越界

# 最大长度为
print(len(str1)-1)

# 3、字符串的索引的切片
# [start:end,step]    # 包头不包尾
# start,end都可以为负数，且end可以超过字符串长度的最大值
# start，end可以省略的
# step默认值为1，start +1 作为第二次取值的索引值
# step为-1 表示从后面往前面取值


# 获取前两个字符

print(str1[0:2])    # ji

# 获取除了后两个字符串的其他字符
print(str1[0:-2])    # jianghuyixi

# 间隔一个取数据
print(str1[::2])        # 间隔两个取    jaguiio

# 切片的end可以超过len(str1)-1

print(str1[1:111])      # ianghuyixiao

# 获取整个字符串(复制字符串)
print(str1[::])         # jianghuyixiao
print(str1[:])         # jianghuyixiao


# 4、字符串的倒序
print(str1[::-1])       # oaixiyuhgnaij