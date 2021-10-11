# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/11 10:18
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1，添加一个 yaml 配置文件，定义用例文件名，服务器地址，服务器端口， 数据库地址，数据库端口，数据库名称，数据库用户名，数据库密码。

# 2， 通过函数封装 pyyaml 读取 yaml 文件数据的操作

# 3，使用封装好的函数读取文件中的配置选项。


# 函数封装
    # 1、函数参数
    # 2、函数逻辑
    # 3、函数返回值
import yaml
def read_yaml(yamlfile):

    '''

    :return:
    '''
    with open(yamlfile,mode='r',encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

if __name__ == '__main__':
    print(read_yaml('case.yaml'))