# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/15 11:11
# @Software       : PythonFullStack
# @Python_verison : 3.7


# 1、mode='w'
with open('write.txt',mode='w',encoding='utf-8')as f:
    f.write('江湖一笑')         # 江湖一笑

# 2、写完后，文件的光标默认在首行，再次写入的话，会把之前的内容全部覆盖
with open('write.txt',mode='w',encoding='utf-8')as f:
    f.write('反反')



# 3、所以需要追加文件的话使用mode='a',在原有文件光标处追加
with open('write.txt',mode='a',encoding='utf-8')as f:
    f.write('反反')

# 4、如果之前没有这个文件则创建改文件

with open('write_end.txt',mode='a',encoding='utf-8')as f:
    f.write('反反')