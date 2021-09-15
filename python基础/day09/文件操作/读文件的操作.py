# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/14 20:09
# @Software       : PythonFullStack
# @Python_verison : 3.7

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)



# 1、mode默认值为'r'，如果文件中有中文则需要在open函数中添加encoding的参数值为utf-8，不区分大小写
f = open('read.txt',mode='r')
print(f.read())             # UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 30: illegal multibyte sequence

# 2、encoding=’utf-8‘
f = open('read.txt',mode='r',encoding='utf-8')
print(f.read())             #

# 3、读的文件不在当前执行文件的路径下。
f = open('test.txt',mode='r',encoding='utf-8')
print(f.read())                 #FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


# 4、传入文件路径解决读的文件不在当前目录下
f = open(r'F:\PythonFullStack\01 python基础\day09\homework\test.txt',mode='r',encoding='utf-8')
print(f.read())

# 5、我们上面的文件操作都没有关闭文件句柄，应该是要关闭文件句柄的，以免占用资源
f = open(r'F:\PythonFullStack\01 python基础\day09\homework\test.txt',mode='r',encoding='utf-8')
print(f.read())
f.close()    # 关闭后，再取读，是取不到文件值的
print(f.read())

# *******************************************************************************
# 6、最好的对文件操作的方式是使用with open(),这种方式会自动关闭文件句柄，不需要手动关闭
# *******************************************************************************
with open('read.txt',mode='r',encoding='utf-8') as f:
    print(f.read())

# 7、readlines,一行一行读取文件
with open('read.txt',mode='r',encoding='utf-8') as f:
    for i in f.readlines():
        print(i.strip())