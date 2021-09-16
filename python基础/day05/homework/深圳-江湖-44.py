# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 8:53
# @Software       : PythonFullStack
# @Python_verison : 3.7

# if
# 题目：
# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣；
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣和最终价格。
# 输入:
# price = xxx
# 输出:
# 购买折扣：8 折
# 优惠价格：xxx 元
# 方法1：
# price = int(input('请输入你的商品价格是：'))
# if 50<= price <=100:
#     discount = 0.9
#     print(f'购买价折扣：9折\n优惠价格：{price - price*discount}')
# elif price>100:
#     discount = 0.8
#     print(f'购买价折扣：8折\n优惠价格：{price - price*discount}')
# else:
#     print(f'购买价折扣：零折\n优惠价格：0')

# 方法2：格式化
# price = int(input('请输入你的商品价格是：'))
# if 50<= price <=100:
#     discount = 0.9
#     info = f'''
#     购买价折扣：{discount*10}折
#     优惠价格：{price*discount}
#     '''
#     print(info)
# elif price>100:
#     discount = 0.8
#     info = f'''
#     购买价折扣：{discount*10}折
#     优惠价格：{price*discount}
#     '''
#     print(info)
# else:
#     discount = 1
#     info = f'''
#     购买价折扣：{discount*10}折
#     优惠价格：{price*discount}
#     '''
#     print(info)


# 题目：闰年判断
# 输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”。
# 什么是闰年，需要自己了解（需求文档没有解释）
# 能被4整除却不能被100整除或能被400整除的年份是闰年.
# year = int(input('请输入一个有效的年份：'))
# if (year%4==0 and year%100 !=0) or (year%400==0):
#     print(f'{year}年是闰年')
# else:
#     print(f'{year}年不是闰年')

# 题目：
#
# 求三个整数中的最大值
a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
c = int(input('请输入第三个数：'))
if a >= b:
    if a >=c:
        print('最大的数是:',a)
    else:
        print('最大的数是:', c)
elif a < b:
    if b >= c:
        print('最大的数是:', b)
    else:
        print('最大的数是:', c)
