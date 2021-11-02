# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/29 16:28
# @Software       : PythonFullStack
# @Python_verison : 3.7

import pymysql

class DBHandler():
    def __init__(self,host='8.129.91.152',user='future',password='123456',database='futureloan',port=3306):
        '''
        初始化设置数据库连接信息,定义host、user、password、database、port为实例属性，这样就可以随着传入的参数不同的，值不同
        '''
        self.host =host
        self.user =user
        self.password = password
        self.database = database
        self.port =port

        # 定义为一个实例说是对象属性self.conn，这样在其他函数（query_one,query_all）中就可以使用
        self.conn = pymysql.connect(host=host,user=user,password=password,database=database,port=port)

        # 放上面容易出现对一个游标进行多次操作
        # self.cursor = self.conn.cursor()

    def query_all(self,sql):
        '''获取多条记录'''
        self.cursor = self.conn.cursor()
        # 提交，每次执行操作之前进行操作前的数据备份
        self.conn.commit()
        # sql = 'select id,reg_name member;'
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def query_one(self,sql):
        '''获取一条记录'''
        self.cursor = self.conn.cursor()
        # 提交，每次执行操作之前进行操作前的数据备份
        self.conn.commit()
        # sql = 'select id,reg_name member;'
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    def close(self):
        '''关闭连接和游标'''
        self.conn.close()


if __name__ == '__main__':
    db1 = DBHandler()
    sql = 'select id,reg_name from member limit 4;'
    print(db1.query_one(sql))
    print(db1.query_all(sql))
    db1.close()