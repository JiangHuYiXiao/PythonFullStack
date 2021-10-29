# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/26 20:43
# @Software       : PythonFullStack
# @Python_verison : 3.7


# python操作数据库步骤：
    # 创建连接打到一个数据库对象
    # 创建游标
    # 使用游标操作数据库
    # 获取游标操作数据库的结果
    # 关闭游标
    # 关闭连接
    # ***********************注意尽量不要对同一个游标进行操作************************
import pymysql


# 创建连接，得到数据库对象
host = '8.129.91.152'
user = 'future'
password = '123456'
database= 'futureloan'
port = 3306
conn = pymysql.connect(host=host,user=user,password =password,database=database,port =port)
print(conn)

# 创建游标,理解为一个操作数据库的光标
cursor = conn.cursor()
print(cursor)

# 使用游标操作数据库
sql = 'SELECT id,reg_name FROM MEMBER LIMIT 5;'
res = cursor.execute(sql)
print(res)    # 5


# 获取游标执行后的结果
# 多条，存储在元组当中
print(cursor.fetchall())

# 单条
print(cursor.fetchone())        # None,
# 因为前面的fetchall已经获取了全部结果，游标cursor已经停留在最后一行了，所以如果真实要获取一条先使用fetchone
# 所以我们以后尽量不要对同一个游标里面进行多次操作，搞两个游标

# 使用多个游标避免对同一个游标操作的数据问题
cursor2 = conn.cursor()
sql = 'SELECT id,reg_name FROM MEMBER LIMIT 5;'
res = cursor2.execute(sql)
print(cursor2.fetchone())

# 关闭游标
cursor.close()
cursor2.close()

# 关闭连接
conn.close()