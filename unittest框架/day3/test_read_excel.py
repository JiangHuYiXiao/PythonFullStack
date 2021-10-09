# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 20:40
# @Software       : PythonFullStack
# @Python_verison : 3.7

'''
进行单元测试就是对我们写的代码进行测试，也就是对我们写的函数或者类中的方法进行测试

比如我们前面写的read_excel_dict模块进行测试
对函数、方法测试步骤
1、准备测试数据，函数的参数
2、准备预期结果
3、调用被测函数，得到实际结果
4、对实际结果和预期结果进行断言，判断用例是否执行成功



但是我们实际工作中，不会有那么多时间精力对自己编写的代码进行这样的测试，
我们会在代码所在的文件中，这样进行一个简单地测试
if __name__ == '__main__':
    read_excel_dict(file,sheet_name)
'''
import unittest
from unittest框架.day2.python读取excel操作封装 import read_excel_dict

class Test_read_excel_dict(unittest.TestCase):
    # @unittest.skip
    def test_read_excel1(self):
        '''
        读取excel中的所有的数据
        :return:
        '''
        file= 'login_data1.xlsx'
        sheet_name = 'Sheet1'
        expected = [{'id': 1, 'title': 'test1', 'data': 'jianghu', 'expected': '成功'}, {'id': 2, 'title': 'test2', 'data': 'yixiu', 'expected': '失败'}, {'id': 3, 'title': 'test3', 'data': 'hhhh', 'expected': '成功'}]

        actual = read_excel_dict(file,sheet_name)
        self.assertEqual(expected,actual)


    def test_read_excel2(self):
        '''
        读取excel中的第二行数据
        :return:
        '''
        file= 'login_data1.xlsx'
        sheet_name = 'Sheet1'
        expected = {'id': 2, 'title': 'test2', 'data': 'yixiu', 'expected': '失败'}

        actual = read_excel_dict(file,sheet_name)
        run_actual = actual[1]
        print(run_actual)
        self.assertEqual(expected,run_actual)

    def test_read_excel3(self):
        '''
        读取excel中的所有的数据,用例执行失败，预期结果和实际结果不相等
        :return:
        '''
        file= 'login_data1.xlsx'
        sheet_name = 'Sheet1'
        expected = [{'id': 11, 'title': 'test1', 'data': 'jianghu', 'expected': '成功'}, {'id': 2, 'title': 'test2', 'data': 'yixiu', 'expected': '失败'}, {'id': 3, 'title': 'test3', 'data': 'hhhh', 'expected': '成功'}]
        actual = read_excel_dict(file,sheet_name)
        self.assertEqual(expected,actual)

