# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/22 10:36
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 封装读取excel的操作函数
    # 1、准备参数
    # 2、准备函数体
    # 3、确定返回值

import openpyxl

def read_excel(file,sheetname):
    # 创建wb对象
    wb = openpyxl.load_workbook(filename=file)
    # 获取sheet页
    sheet_name= wb[sheetname]

    # 获取sheet也得所有数据
    res = list(sheet_name.values)
    # excel首行标题后面行
    row = res[1:]
    # 组装数据为字典格式
    data = [dict(zip(res[0],i)) for i in row]

    # 返回数据
    return data


if __name__ == '__main__':
    res =read_excel(r'F:\PythonFullStack\API接口测试\day4\api接口框架\data\cases2.xlsx', 'recharge')

    print(res,type(res))
    # print(res['data'])