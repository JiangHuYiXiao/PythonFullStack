# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/9 15:26
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目：现在有字符串：
str1 = 'python cainiao 666'

# 请使用代码找出第 5 个字符
# 请复制一份字符串，保存在变量 str_two 当中

print(str1[4])
str_two = str1[:]
str_two1 = str1[0:]
print(str_two)
print(str_two1)


# 题目：卖橘子的计算器

# 写一段代码，用户输入橘子的价格，和重量，计算出应该支付的金额！（提示：不需要校验数据，默认传入数字就可以了。
# 使用input函数获取用户输入哦，并且input 得到的数据都是字符串类型）

# price = input("请输入价格")
# weight = input("请输入重量")
price = int(input('请输入每斤橘子价格:'))
weight = int(input('请输入多少斤橘子重量:'))
money = price * weight
print(f'付款{money}元')


# 题目：字符串综合演练 my_hobby = "Never stop learning!"
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”）；“索引”指的是字符的索引值
# （比如索引0， 代表的是第一个字符“N”）；开始位置 ，是指字符串起始，即下标为0开始；末尾，是指字符串最后。
# 截取从 位置2 ~ 位置6 的字符串(含 位置6)
# 截取完整的字符串
# 从 索引3 开始，每2个字符中取一个字符
# 截取字符串末尾两个字符
# 字符串的倒序
my_hobby = "Never stop learning!"
print(my_hobby[1:6])            # ever
print(my_hobby[:])              # Never stop learning!
print(my_hobby[3::2])           # e tplann!
print(my_hobby[-2:])           # g!
print(my_hobby[::-1])           # !gninrael pots reveN



# 题目：以下哪个是正确的字符串（B,D）

# A ‘abc”ab” B ‘abc”ab’ C “abc”ab” D “abc\”ab”    \表示转义，不是字符串


# AA1 = 'abc"a"
AA2 = 'abc"a'
# AA3 = "abc"a"
AA4 = "abc\"a"
print(type(AA2),AA2,type(AA4),AA4)





# 题目：“ab”+”c”*2 结果是：（C）

# A abc2 B abcabc C abcc D ababcc

print("ab"+"c"*2)