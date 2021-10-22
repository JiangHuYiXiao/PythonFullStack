# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/15 16:07
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 函数封装步骤
# 1、函数参数
# 2、函数逻辑体
# 3、函数的返回值
from loguru import logger
from API接口测试.day4.api接口框架.config.config import log_file
def at_logger(file):
    logger.add(sink=file, encoding='utf-8', rotation='100MB', level='INFO')
    return logger

my_log = at_logger(log_file)

if __name__ == '__main__':

    at_logger('test.log').info('正常信息')


