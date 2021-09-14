# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 18:56
# @Software       : PythonFullStack
# @Python_verison : 3.7
'''
# 题目：删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 方法1
info.remove('矮穷丑')
print(info)

# 方法2：
index = info.index('矮穷丑')
info.pop(index)
print(info)

# 方法3：
index = info.index("矮穷丑")
del(info[index])
print(info)



# 题目：现在有一个列表 li2=[1，2，3，4，5]，请通过相关的操作改成 li2 = [0，1，2，3，66，4，5，11，22，33]。
li2=[1,2,3,4,5]
li2.insert(0,0)
print(li2)
li2.insert(4,66)
print(li2)
li2.extend([11,22,33])
print(li2)



# 题目：使用列表存储和操作以下数据
#
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
#
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
#
# c, 平台为了保护你的隐私，需要你删除你的联系方式；

info_list = ['江湖一笑','男',22]
info_list.append(170)
info_list.append(18270717375)
print(info_list)
info_list.pop(-1)
print(info_list)


# 题目：将字符串"I Love Java" 重新定义成"I Love Python"

java= "I Love Java"
print(java.replace('Java', 'Python'))
print(java)
'''



# 题目：将字符串中的单词位置反转
# “hello xiao mi” 转换为 “mi xiao hello” （提示：通过字符串分割，拼接，列表反序等知识点来实现）
mi = "hello xiao mi"
# 字符串转换成列表使用split()

mi_list = (mi.split(' '))

# 列表数据进行反转使用reverse(),改变的是原列表mi_list
mi_list.reverse()

# 列表数据转换成字符串使用join()
mi_reverse = ' '.join(mi_list)

print(type(mi_reverse),mi_reverse)          # <class 'str'> mi xiao hello





# 题目：字符串格式化
# 把姓名、年龄、密码、性别、专业、爱好分别存储在变量中，用下列格式展示：
# age = 18
# ...
#
# 显示效果：
# -------------------------------
# 姓名：xxx
# 年龄：xxx
# 密码：xxx
# 性别：xxx
# 专业：xxx
# 爱好：xxx
# -------------------------------

age = 18
name = '江湖一笑'
password = '123456'
sex = '男'
professional = 'IT'
like = '茅台'

info = f'''
-------------------------------
姓名：{name}
年龄：{age}
密码：{password}
性别：{sex}
专业：{professional}
爱好：{like}
-------------------------------
'''
print(info)
