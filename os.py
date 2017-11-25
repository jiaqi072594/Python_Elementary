# -*- coding: utf-8 -*-
import os
'''
os.getced() #查询当前目录
os.chdir('目录，\\') #修改当前工作目录路径
os.makedirs() #创建新文件夹
'''
'''
#处理绝对路径和相对路径
调用os.path.abspath(path) 将返回参数的绝对路径的字符串，此为将相对路径转换为绝对路径的简便方法
调用os.path.isabs(path) 如果参数是一个绝对路径，就返回True，如果参数是一个相对路径，则返回False
调用os.path.relpath(path,start) 将返回从start路径到path的相对路径的字符串。如果没有提供start，就使用当前工作目录作为开始路径
调用os.path.dirname(path) 将返回一个字符串，它包含path参数中最后一个斜杠之前的所有内容
调用os.path.basename(path) 将返回一个字符串，它包含path参数中最后一个斜杠之后的所有内容
path.split(os.path.sep)返回一个list，内容是路径 OS X和linux系统上返回的列表头上有一个空字符

#查看文件大小和文件夹内容
调用os.path.getsize(path)将返回path参数中文件的字节数
调用os.listdir(path) 将返回文件名字符串的列表，包含path参数中的每个文件

#检查路径有效性
如果path参数所指的文件或文件夹存在，调用os.path.exists(path)将返回True，否则返回False
如果path参数存在，并且是一个文件，调用os.path.isfile(path)将返回True，否则返回False
如果path参数存在，并且是一个文件夹，调用os.path.isdir(path)将返回True，否则返回False
'''
'''
#永久删除文件和文件夹
    用os.unlink(path)将删除path处的文件
    调用os.rmdir(path)将删除path出的文件夹，该文件夹必须为空，其中没有任何文件和文件夹。

'''
'''
#遍历目录树
    os.walk()函数被传入一个字符串值，即一个文件夹的路径。可以在一个for循环语句中使用os.walk(函数)，遍历目录树，就想使用range()函数遍历一个范围的数字一样。不想range(),os.walk()在循环的每次迭代中，返回3个值：
    1 当前文件夹名称的字符串
    2 当前文件夹中子文件夹的字符串的列表
    3 当前文件夹中文件的字符串的列表
    所谓当前文件夹，是指for循环当前迭代的文件夹。程序的当前工作目录，不会因为os.walk()而改变
    通常使用foldername subfolders和filenema来命名这三个变量

'''