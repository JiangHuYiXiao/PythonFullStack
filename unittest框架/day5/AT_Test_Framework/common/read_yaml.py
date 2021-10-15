# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 16:32
# @Software       : PythonFullStack
# @Python_verison : 3.7
import yaml
def read_yaml(yamlfile):

    '''
data
    :return:
    '''
    with open(yamlfile,mode='r',encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

if __name__ == '__main__':
    print(read_yaml('case.yaml'))