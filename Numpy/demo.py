# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:30:40 2017

@author: MOOM
"""

import numpy as np
print(np.version.version)

'''
使用numpy.array方法
'''
#以list或tuple变量为参数产生一维数组：
print(np.array((1.2, 2, 3, 4)))
print(np.array([1.2, 2, 3, 4]))
print(type(np.array((1.2, 2, 3, 4))))
#以list或tuple变量为元素产生二维数组：
print(np.array([[1,2],[3,4]]))
#生成数组的时候，可以指定数据类型，例如numpy.int32, numpy.int16, and numpy.float64等：
print(np.array((1.2, 2, 3, 4),dtype = np.int32))

'''
使用numpy.arange方法
'''
print( np.arange(15))
print( type(np.arange(15)))
print( np.arange(15).reshape(3, 5))
print( type(np.arange(15).reshape(3, 5)))

'''
使用numpy.linspace方法
'''
#例如，在从1到3中产生9个数：
print('>np.linspace(1, 3, 9) =\n',np.linspace(1, 3, 9))

'''
使用numpy.zeros，numpy.ones，numpy.eye等方法可以构造特定的矩阵
'''
print( '>np.zeros((3,4)) =\n',np.zeros((3,4)))
print( '>np.ones((3,4)) =\n',np.ones((3,4)))
print ('>np.eye(3) =\n',np.eye(3))
#创建一个三维数组：
print (np.zeros((2,2,2)))

'''
获取数组的属性：
'''
a = np.zeros((2,2,2))
print ('>np.zeros((2,2,2)) =\n',a)
print ('>数组的维数\n',a.ndim)   #数组的维数
print ('>数组每一维的大小\n',a.shape)  #数组每一维的大小
print ('>数组的元素数\n',a.size)   #数组的元素数
print ('>元素类型\n',a.dtype)  #元素类型
print ('>每个元素所占的字节数\n',a.itemsize)  #每个元素所占的字节数

'''
数组索引，切片，赋值
'''
a = np.array( [[2,3,4],[5,6,7]] )
print('>np.array( [[2,3,4],[5,6,7]] )\n',a)
print('>a[1,2]\n',a[1,2])
print('>a[1,:]\n',a[1,:])
print('>a[1,1:2]\n',a[1,1:2])
a[1,:] = [8,9,10]
print('>a[1,:] = [8,9,10]\n',a)

'''
使用for操作元素
'''
for x in np.linspace(1,3,3):
    print('>for x in np.linspace(1,3,3):\n',x)

'''
基本的数组运算
'''
#先构造数组a、b：
a = np.ones((2,2))
b = np.eye(2)
print(a)
print(b)
#数组的加减乘除：
print ((a > 2))
print (a+b)
print (a-b)
print (b*2)
print ((a*2)*(b*2))
print (b/(a*2))
print ((a*2)**4)
 # 使用数组对象自带的方法：
a.sum()
a.sum(axis=0)   #计算每一列（二维数组中类似于矩阵的列）的和
a.min()
a.max()
#使用numpy下的方法：
np.sin(a)
np.max(a)
np.floor(a)
np.exp(a)
np.dot(a,a)   ##矩阵乘法

'''
合并数组
'''
#使用numpy下的vstack和hstack函数
a = np.ones((2,2))
b = np.eye(2)
print (np.vstack((a,b)))
print (np.hstack((a,b)))
#看一下这两个函数有没有涉及到浅拷贝这种问题：
c = np.hstack((a,b))
print (c)
a[1,1] = 5
print(c)
#可以看到，a、b中元素的改变并未影响c。

'''
深拷贝数组
'''
#数组对象自带了浅拷贝和深拷贝的方法，但是一般用深拷贝多一些：
a = np.ones((2,2))
b = a
c = a.copy()  #深拷贝
c is a

'''
基本的矩阵运算
'''
#转置：
a = np.array([[1,0],[2,3]])
print (a)
print (a.transpose())
#迹：
print (np.trace(a))
#numpy.linalg模块中有很多关于矩阵运算的方法：
import numpy.linalg as nplg
#特征值、特征向量：
print (nplg.eig(a))

 



