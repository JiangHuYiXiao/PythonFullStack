# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/9 11:15
# @Software       : PythonFullStack
# @Python_verison : 3.7
# 2 - 3 + 4 - 5 + 6 ... + 100
# 用户输入考试成绩，当分数高于90（包含90）时打印A；
# 否则如果分数高于80（包含80）时打印B；
# 否则如果当分数高于70（包含）时打印C；
# 否则如果当分数高于60（包含60）时打印D；
# 其他情况就打印E

# in_score = int(input('请输入你的考试成绩：'))
#
# if in_score >= 90:
#     print('考试成绩级别为A')
# elif 80<=in_score<90:
#     print('考试成绩级别为B')
# elif 70<=in_score<80:
#     print('考试成绩级别为C')
# elif 60<=in_score<80:
#     print('考试成绩级别为D')
# else:
#     print('考试成绩级别为E')


# 编写如下程序

# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）
# def double_money(money):
#     add_money = 0.0352
#     total_money = 2*money
#     year = 1
#     while money < total_money:
#         money =  money*(1+add_money)
#         print(money)
#         year += 1
#         print(year)
#     return year
#
# print(double_money(100))


# save_money = float(input("请输入你要存入银行的钱："))
#
# print("你存了{}元到银行!".format(save_money))
#
# TOTAL_MONEY = save_money * 2   # 定义变量用于保存总钱数
#
# year = 1    # 定义变量用于记录年份
#
# while save_money < TOTAL_MONEY:
#
#     save_money *= (1 + 0.0352)
#     print(save_money)
#
#     year += 1
#     print(year)
#
# print("定期利率为3.52%，需要{}年本金和才能翻一番。".format(year))

# print(double_money(10))

from loguru import logger

try:
    assert (1==6)
except AssertionError as e:
    # error日志一般放在会出错的代码之后
    logger.error('用例1断言失败')
    # 捕获了异常后，必须抛出，否则不会记录到错误信息
    raise e
print('****************************************')
