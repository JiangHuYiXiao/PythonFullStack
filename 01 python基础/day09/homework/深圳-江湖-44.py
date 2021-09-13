# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/13 9:04
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目：BMI 计算
# 使用函数完成以下操作
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
# def get_bmi(height, weight):
'''
def cal_bmi(height,weight):
    bmi = weight / (height ** 2)
    if (0 < bmi < 18.5):
        return (f'你的BMI值为{bmi}\n过轻,请多吃，补充营养')
    elif (18.5 <= bmi < 25):
        return(f'你的BMI值为{bmi}\n正常,请保持')
    elif (25 <= bmi < 28):
        return(f'你的BMI值为{bmi}\n过重,请多锻炼')
    elif (28 <= bmi < 32):
        return(f'你的BMI值为{bmi}\n肥胖,请控制饮食，多锻炼')
    elif bmi >= 32:
        return(f'你的BMI值为{bmi}\n严重肥胖,请控制饮食，多锻炼')
    else:
        return('数据错误')



print(cal_bmi(1.7, 15))
print(cal_bmi(1.7, 65))
print(cal_bmi(1.7, 80))
print(cal_bmi(1.7, 90))
print(cal_bmi(1.7, 200))
print(cal_bmi(1.7, 0))




# 题目：挑选足球运动员
#
# 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
#
# 编写一个程序，根据用户的姓名，性别和年龄，打印这个人是否可以加入球队，询问10次后，打印满足条件的所有人的名字。
#
# （要求：定义函数处理逻辑)
def football_girls():
    list = []
    for i in range(10):
        name = input('请输入你的姓名:')
        sex = input('请输入你的性别:')
        age = int(input('请输入你的年龄:'))
        if sex == '女' and 15 <= age <= 22 and name not in list:
            list.append(name)
            print('可以加入球队')
        else:
            print('不可以加入球队')
    return list
print(football_girls())

'''


# 题目：列表和字典数据类型转换
#
# # 有一组用例数据如下：
# cases = [
#   ['case_id', 'case_title', 'url', 'data', 'excepted'],
#   [1, '用例1', 'www.baudi.com', '001', 'ok'],
#   [4, '用例4', 'www.baudi.com', '002', 'ok'],
#   [2, '用例2', 'www.baudi.com', '002', 'ok'],
#   [3, '用例3', 'www.baudi.com', '002', 'ok'],
#   [5, '用例5', 'www.baudi.com', '002', 'ok'],
# ]
# ​
# # 要求一：把上述数据转换为以下格式
# res1 = [
#   {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#   {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]
# ​
# # 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
# res = [
#   {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#   {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]


def change_list(cases):
    res1 = []
    res = []
    for i in range(len(cases)):
        if i+1<len(cases):
            res1.append(dict((zip(cases[0], cases[i+1]))))
    for j in res1:
        if j['case_id'] > 3:
            res.append(j)
    print(res)
    return res1

cases = [
        ['case_id', 'case_title', 'url', 'data', 'excepted'],
        [1, '用例1', 'www.baudi.com', '001', 'ok'],
        [4, '用例4', 'www.baudi.com', '002', 'ok'],
        [2, '用例2', 'www.baudi.com', '002', 'ok'],
        [3, '用例3', 'www.baudi.com', '002', 'ok'],
        [5, '用例5', 'www.baudi.com', '002', 'ok'],
    ]
print(change_list(cases))