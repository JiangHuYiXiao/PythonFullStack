# @Author         : 江湖一笑
# @Time           : 2021/9/8 8:58
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 题目1：
# 编写如下程序：

# a.用户输入1-7七个数字，分别代表周一到周日；

# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”

# c.如果输入0，退出循环

# d.输入其他内容，提示：“输入有误，请重新输入！”

# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。
# while True:
#     day = int(input('请输入1-7之间的数字:'))
#     if day >=1 and day <=5 :
#             if day ==1:
#                 print('周一')
#             if day ==2:
#                 print('周二')
#             if day == 3:
#                 print('周三')
#             if day == 4:
#                 print('周四')
#             if day == 5:
#                 print('周五')
#     elif day == 6 or day == 7:
#         print('周末')
#     elif day == 0:
#         break
#     else:
#         print('你输入的有误，请重新输入')


# 方法2：
# 定义一个列表，因为列表也是用来存储数据的，而且是存储有序的数据的。还可以用字典来存储。
dict = {'1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周末','7':'周末'}
while True:
    day = input('请输入1-7之间的数字:')
    if day in dict:
        print(dict[day])
    elif day == '0':
        break
    else:
        print('输入有误，请重新输入')











# 题目：使用for循环打印九九乘法表
#
# 提示：使用双层 for 的 range 嵌套， 每项数据之间空一个Tab键，可以使用 print("数字", end='\t'),  print() 无参数可以打印换行
'''
1 * 1 = 1

1 * 2 = 2    2 * 2 = 4

1 * 3 = 3    2 * 3 = 6      3 * 3 = 9

1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16

1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25

1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36

1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49

1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64

1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9
'''
#
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f'{b} * {a} = {a * b}', end='\t')
#         if a == b:
#             print()

# 题目：编写程序实现，
# 在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”，
# 小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了！”，其中N是用户输入数字的次数。
# 提示：使用while无限循环，当猜中时break

# num_key = 6
# i = 0
# while True:
#     input_number = int(input('请输入0~9之间的整数：'))
#     i += 1
#     if input_number > num_key:
#         print('遗憾，太大了')
#     elif input_number < num_key:
#         print('遗憾，太小了')
#     elif input_number == num_key:
#         print(f'预测{i}次，你猜中了')
#         break
#     else:
#         print('你输入的有误，请重新输入')


# 题目：实现冒泡排序（不要求提交，面试之前背熟，什么是冒泡排序需要自己了解）
#
# 具体需求：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
#
# 编码提示：
#
# 1、先写出第一轮比较的代码哦。如在a当中，将最大的一个数据放在列表最后。
#
# 2、再写出第二轮比较的代码：在1之后的列表当中，将第二大的数据，放在列表的倒数第二
#
# 3、以此类推
#
# 4、比对以上所写的代码，有何相同，有何不同之处。再考虑使用外层for来替换

# 第一轮的比较结果：[1, 4, 7, 34, 2, 89]
# list = [1,7,4,89,34,2]
# for i in range(len(list)-1):
#     if list[i] > list[i+1]:
#         list[i],list[i+1] = list[i+1],list[i]
# print(list)

# list1 = [1, 4, 7, 34, 2, 89]
# # 第二轮的比较结果：
# for i in range(len(list1)-1):
#     if list1[i] > list1[i+1]:
#         list1[i],list1[i+1] = list1[i+1],list1[i]
# print(list1)


# list2 =[1, 4, 7, 2, 34, 89]
# # 第三轮的比较结果：
# for i in range(len(list2)-1):
#     if list2[i] > list2[i+1]:
#         list2[i],list2[i+1] = list2[i+1],list2[i]
# print(list2)


# # 第四轮的比较结果
# list3 =[1, 4, 2, 7, 34, 89]
# # 第三轮的比较结果：
# for i in range(len(list3)-1):
#     if list3[i] > list3[i+1]:
#         list3[i],list3[i+1] = list3[i+1],list3[i]
# print(list3)

# 外循环5次，内循环4次
# 归纳后为：
# list = [1,7,4,89,34,2]
# for i in range(len(list)-1):
#     for j in range(len(list)-1-i):
#         if list[j] > list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
# print(list)

'''
分行赋值和单行赋值

# 赋值前：
print(id(list[0]))   # 8790923465760
print(id(list[1]))   # 8790923465952

# 赋值后

list[0] = list[1]
print(id(list[0]))   # 8790923465952

list[1] = list[0]
print(id(list[1]))   # 8790923465952

# 赋值方式2：
# 赋值后
# list[0],list[1] = list[1],list[0]
# print(id(list[0]))   # 8791121974496
# print(id(list[1]))   # 8791121974304
'''