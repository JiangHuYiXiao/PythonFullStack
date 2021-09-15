# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 20:09
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目：把以下字典分行添加到文件当中：
person_info = [
  {
      "name": "vvv",
      "age": 22,
      "gender": "男",
      "hobby": "学习",
      "motto": "学习使我快乐"
  },
  {
      "name": "yuze",
      "age": 20,
      "gender": "女",
      "hobby": "拿30K offer",
      "motto": "下次拿个40K 的"
  }
]
# 得到一个 info.txt 的文件：
# name,age,gender,hobby,motto
# vvv,22,男,学习, 学习使我快乐
# yuze,20,女,拿30K offer,下次拿个40K 的

# def person_info_to_file(person_info):
#     line1 = []
#     for i in person_info[0].keys():
#         line1.append(i)
#     f = open('info.txt', mode='a', encoding='utf-8')
#     f.write(','.join(line1))
#     f.write('\n')
#     for j in range(len(person_info)):
#         for value in person_info[j].values():
#             f.write((str(value)+',').strip(','))
#         f.write('\n')
#     f.close()
# person_info_to_file(person_info)


# 题目：手工创建cases.txt 文件，文件中手工复制 2 行数据：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

# 请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）
# [
#   {
#       'url':'/futureloan/mvc/api/member/register',
#       'mobile':'18866668888',
#       'pwd':'123456'
#   },
#   {
#       'url':'/futureloan/mvc/api/member/recharge',
#       'mobile':'18866668888',
#       'amount':'1000'
#   }
# ]

def read_file_to_list():
    list =[]
    # dict1 = {}  不能在循环外定义，否则操作的是同一个字典
    with open('cases.txt',mode='r',encoding='utf-8') as file:
        for i in file.readlines():
            i2 = i.strip().split('@')
            dict1 = {}              # 这里定义相当于，每一行循环一次时，会生成一个新的字典
            for j in i2:
                i3 = j.split(':')
                dict1[i3[0]]= i3[1]
            list.append(dict1)
        return list

print(read_file_to_list())
