# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/9/16 8:55
# @Software       : PythonFullStack
# @Python_verison : 3.7

score = 100
age = 1
if score == 100:
    print('厉害了')
    if age <=1:
        print('神童哦')
    else:
        print('普通人')

else:
    print('努力学习，天天吃肉')

# debug调试总结
# 1、想要debug必须打断点，（pycharm中函数定义的时候打断点是没有用的的）。
# 2、使用step over，进行调试时候，如果遇到有子函数时，不会一步步跳转到子函数中运行，而是会直接运行整个子函数
# 3、Step Into：单步执行，遇到子函数就进入并且继续单步执行（简而言之，进入子函数）。
# 4、Step Into My Code：进入自己编写的函数，不进入系统函数，很少用到。
# 5、通过debug我们可以查看到变量的值变化，在variables会输出，或者在文件中会标记
# 6、可以通过evaluate计算器，计算变量的值