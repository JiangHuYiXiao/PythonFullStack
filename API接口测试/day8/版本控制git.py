# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/11/1 9:27
# @Software       : PythonFullStack
# @Python_verison : 3.7

# 1、git版本控制的作用：
    # 回滚版本
    # 代码溯源

# 2、git和svn的区别，git是有本地仓库的，先保存到本地仓库，不用每次提交到远程仓库，svn每次都要提交到远程仓库


# 3、代码如何上传到github、gitlab、gitee？
# 先把代码保存到本地使用add和commit，然后使用push上传到远程仓库上


# 4、如何把远程代码拷贝到本地
    # 如果本地没有改项目的任何代码则使用clone
    # 如果本地有该项目的一些代码，则使用pull把远程仓库的代码更新过来


# 5、项目上传到gitee代码过程
# 切换到需要进行版本控制的目录下打开
# git init 在本地创建git仓库
# 使用git status命令查看仓库下的文件状态  可以查看哪些文件没有被追踪untracked files present
# 使用git add 文件名   --添加文件到可以追踪后，可以再次使用git status就可以查看到文件已经添加到了版本控制中然后可以commit了到本地仓库了
# 使用git add .   添加目录下的所有文件到版本控制中
# 使用git commit -m "v1"提交目录下的所有文件到本地仓库
# 使用命令：git remote add origin https://gitee.com/jianghuyixiao/api_framwork.git
#          git push -u origin master   提交本地仓库代码到远程仓库


# 6、.gitignore文件作用：写到文件中的内容是不会上传到github，gitee远程仓库中


# 7、同事获取