# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 10:16
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 在python中遇到:下面就要缩进四个空格，表示某个代码块


# 1、简单的if结构
# if 条件:
    # 满足条件执行

# 2、标准的if结构
# if 条件1:
    # 满足条件执行
# elif 条件2：
    # 满足条件2执行
# elif 条件3：
    # 满足条件3执行
# else:
    # 上面所有不满足执行这里

# ***********************************************************************************
# 3、在一个if表达式中，不会执行一个以上的分支，只要遇到有一个满足则后面都分支和else都不执行了。
# 所有if，elif都不满足则执行else
# ***********************************************************************************

# 4、条件的分类
# 条件必须是可以得到bool值

# 比较运算 <= a <=, ==, >,<

# 逻辑运算 and,not

# 成员运算  in,not in



# 5、判断是否为空
# 为空：
# if not (str,list,tuple,dict,set):
# 不为空：
# if (str,list,tuple,dict,set):


a ='kongkong'
if a:
    print('不为空')
elif not a:
    print('空的字符串')

li = []
if li:
    print('不为空')
elif not li:
    print('为空列表')

dict = {}
if dict:
    print('不为空')
elif not dict:
    print('为空字典')


# 6、if ....if结构,是两个if，如果条件满足这两个的if条件，那么两个都会执行
a =5
if a==5:
    print('中间')

if a>1:
    print('大于1')

# 两个都会执行
# 中间
# 大于1

# 、三目运算符
# 成立的结果 if 条件 else 条件不成立的结果
print(a - 1 if a > 1 else a + 1)            # 4