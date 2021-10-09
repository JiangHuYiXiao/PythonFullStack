# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/9 10:53
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1，封装 excel 读取测试用例


from openpyxl import load_workbook

def read_excel_dict(file,sheet_name):
    '''
    :param file:
    :param sheet_name:
    :return: 把excel中的数据返回成一个列表类型
    '''
    # 创建wb对象
    wb = load_workbook(file)

    # 获取sheet页
    sheet1 = wb[sheet_name]

    # list将generator转换成一个list包含所有测试数据
    data = list(sheet1.values)
    row = data[1:]
    # 使用列表推导式
    rows = [dict(zip(data[0], i)) for i in row]
    return rows


# 实际工作中对我们自己编写代码进行一个简单测试是按照下面这个方式进行测试的
if __name__ == '__main__':
    print(read_excel_dict(file='login_data.xlsx', sheet_name='Sheet1'))