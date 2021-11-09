# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/8 9:00
# @Software       : PythonFullStack
# @Python_verison : 3.7

import re
# 这个类建议放在API_Case中，因为我们的测试类都继承了API_Case类，
# 然后最好还是定义为一个类方法，这样，我们不仅可以使用类调用还可以使用对象进行调用类中的方法属性

# 注意注意：使用这个方法进行数据替换，我们必须提前设置好类的同名属性，比如说在setUp，setUpClass中调用函数
# 或者通过在excel中有一列extractor中设置响应返回的结果中的属性名为key，jsonpath表达式为值，然后通过for循环取出key和value，
# 因为我们的key为字符串，所以再通过setattr(prop_name,key,value)去设置类属性
class Data:
    member_id ='123456'
    money = 600

    @classmethod
    def replace_data(cls,string):
        result = re.finditer('#(.*?)#',string=string)
        for el in result:
            old = el.group()
            new = getattr(Data,el.group(1))
            string = string.replace(old,str(new))
        return string

res = Data().replace_data(string= '{"member_id":"#member_id#","amount":#money#}')
print(res)