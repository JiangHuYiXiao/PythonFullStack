# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/13 17:39
# @Software       : PythonFullStack
# @Python_verison : 3.7
import logging



'''
函数封装步骤
1、函数参数
2、函数体中的函数逻辑
3、函数返回值
'''
def at_log(name='root',level='INFO',fmt='%(asctime)s:%(name)s:%(levelname)s:%(lineno)d:%(message)s',file='test.log'):
    # 1、创建一个logging日志收集器，理解为笔
    logger = logging.getLogger(name)          # 括号内为一个标签,可以自定义

    # 设置笔的级别
    logger.setLevel(level)

    # 2、handler，笔记本,把logger笔记输出到控制台
    handler= logging.StreamHandler()

    # 设置handler的级别
    handler.setLevel(level)

    # 3、建立笔和笔记本的关系
    logger.addHandler(handler)

    # 设置命令窗口的输出格式
    consle_fmt = logging.Formatter(fmt=fmt)
    handler.setFormatter(consle_fmt)

    # 4、把日志输出到文件中
    file_handler = logging.FileHandler(file,mode='a',encoding='utf-8')

    # 设置file_handler的级别
    file_handler.setLevel(level)

    logger.addHandler(file_handler)
    # 设置日志文件内容的输出格式
    file_fmt = logging.Formatter(fmt=fmt)
    # file_fmt = logging.Formatter(style='{',fmt='{asctime}:{name}:{levelname}:{lineno}:{message}')           # style默认为%，可以修改为{，或者$
    file_handler.setFormatter(file_fmt)
    # 5、记录日志
    # 因为logging默认级别为warning，所以大于等于warning级别的日志会输出，info级别的就不会输出



    # 6、修改logging的默认级别
    # 不仅需要修改笔的还需要修改笔记本的级别
    return logger

if __name__ == '__main__':
    a = at_log()
    a.info('正常信息')
    a.warning('警告信息')
    a.error('错误信息')
