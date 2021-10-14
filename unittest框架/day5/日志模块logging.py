# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 9:10
# @Software       : PythonFullStack
# @Python_verison : 3.7

# python本身的日志记录模块为logging
# 这个模块的日志记录过程比loguru复杂很多，我们可以把这个模块的日志记录过程理解为用笔在笔记本上写日记

import logging

# 1、创建一个logging日志收集器，理解为笔
logger = logging.getLogger('AT_test')          # 括号内为一个标签,可以自定义

# 设置笔的级别
logger.setLevel('INFO')

# 2、handler，笔记本,把logger笔记输出到控制台
handler= logging.StreamHandler()

# 设置handler的级别
handler.setLevel('INFO')

# 3、建立笔和笔记本的关系
logger.addHandler(handler)

# 4、把日志输出到文件中
file_handler = logging.FileHandler('demo2.log',mode='a',encoding='utf-8')

# 设置file_handler的级别
file_handler.setLevel('INFO')

logger.addHandler(file_handler)

# 5、记录日志
# 因为logging默认级别为warning，所以大于等于warning级别的日志会输出，info级别的就不会输出

logger.info('正常信息')         # 不会输出
logger.error('错误信息')      # 因为logging默认级别为warning，所以这个日志信息会输出
logger.warning('警告信息')      # 因为logging默认级别为warning，所以这个日志信息会输出

# 6、修改logging的默认级别
# 不仅需要修改笔的还需要修改笔记本的级别
