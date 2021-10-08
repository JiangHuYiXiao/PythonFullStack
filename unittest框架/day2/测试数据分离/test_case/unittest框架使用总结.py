# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/10/8 17:07
# @Software       : PythonFullStack
# @Python_verison : 3.7


# 1、测试数据的分离
# 把用例放到test_case包下，报告放到report包中，测试数据放在data包中，运行脚本写在run.py中


# 2、**********************包和目录的区别*******************************
# 包中会有__init__.py文件
# 以后如果目录下面会包含py文件那么就创建包
# ********************************************************************


# 3、unittest框架使用
# 编写用例
    # 把所有的用例放到一个以test_开头的一个统一的包中，然后编写测试用例
    # 测试类需要继承unittest.TestCase
    # 用例断言，不要使用assert，而应该使用unittest框架的，self.assertEqual ，self.assertTrue

# 运行用例          ---> 在run.py文件下运行
    # 使用suite = unittest.defaultTestLoader.discover('./')收集用例
    # 然后运行用例
    # runner = unittestreport.TestRunner(suite,filename='登录测试报告',tester='jianghu',templates=1)
    # runner.run()

# 生成报告
    # 常用的报告模板有unittest自带的，有unittest默认的三种测试报告：HTMLTestRunner,HTMLTestRunner_cn,HTMLTestRunner_PY3
    # 第三方的：unittestreport、beautifulreport


# 4、unittest框架运行方式选择
    # 如果直接运行可能是以python方式运行，因为编辑器pycharm没有识别出来unittest用例
    # 需要手动设置
    # file--->setting ---> 搜索unittest
    # 然后在run...下面如果能够看到unittest开头的则表示会以unittest运行，否则需要进行edit，把python下面的运行都删除，添加Python tests
    # 最后再重新启动编辑器


# 5、pip是python官方的包管理工具，安装、卸载应用需要使用pip
# 因为这个pip默认使用数据源是国外的，有时候网络会比较慢
# 这个时候需要使用国内数据源
# pip install -i http://mirrors.aliyun.com/pypi/simple/ unittestreport