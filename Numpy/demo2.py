# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:35:09 2017

@author: MOOM
"""
'''
Numpy优点：
1.N维数组（矩阵），快速高效，矢量数学运算
2.搞笑的Index，不需要循环
3.开源免费快平台，运行效率足以媲美C/Matlab
'''
#一、数组的创建和访问
'''
#数组创建
import numpy as np
list_1 = [1,2,3,4]
array_1 = np.array(list_1)
print('>array_1 =\n',array_1)
list_2 = [5,6,7,8]
array_2 = np.array([list_1,list_2])
print('>array_2 =\n',array_2)

#数组元素操作
print('>array_2.shape =\n',array_2.shape)#显示array_2的属性（输出表示数组array_2是一个2行4列的数组
print('>array_2.size =\n',array_2.size)#返回数组里面的元素
print('>array_2.dtype =\n',array_2.dtype)#返回数组里面元素的类型
array_3 = np.arange(1,10,2)
print('>array_3 =\n',array_3)
print('>array_3 =\n',np.zeros(5))#返回一个一维全零矩阵
print('>np.zerosd([2,3]) =\n',np.zeros([2,3]))#返回一个二维全零矩阵
print('>np.eye(5) =\n',np.eye(5))#返回一个5*5的单位矩阵，数组元素为float类型

#数组元素访问
a = np.arange(1,10)
print('>a =\n',a)
print('>a[1] =\n',a[1])
print('>a[1:5] =\n',a[1:5])
b = np.array([[1,2,3],[4,5,6]])
print('>b =\n',b)
print('>b[1][0] =\n',b[1][0])
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('>c =\n',c)
print('>c[:2, 1:] =\n',c[:2, 1:])
'''
#二、数组与矩阵运算
'''
#快速创建数组
import numpy as np
np.random.randn(10)#randn创建一个长度为10的一维数组，并且数组里面的值符合标准正态分布
np.random.randint(10)#输出10以内随机一个数字
np.random.randint(10,size=(2,3))#创建2*3的数组，数组元素是10以内随机数字
np.random.randint(10,size=20)#创建长度为20的数组，数组元素是10以内随机数字
np.random.randint(10,size=20).reshape(4,5)#创建长度为20的数组，然后做reshape操作把他变成4*5的数组，数组元素是10以内的随机数字 
#数组运算
a = np.random.randint(10,size=20).reshape(4,5)
b = np.random.randint(10,size=20).reshape(4,5)
print('a =\n',a)
print('b =\n',b)
print('a+b =\n',a+b)
print('a-b =\n',a-b)
print('a*b =\n',a*b)
#print('a/b =\n',a/b)#出现分母为零会报警
#创建矩阵
print('np.mat([[1,2,3],[4,5,6]]) =\n',np.mat([[1,2,3],[4,5,6]]))#创建一个二维矩阵
print('np.mat(a) =\n',np.mat(a))#把数组a转换成矩阵
#矩阵运算
A = np.mat(a)
B = np.mat(b)
print('A+B =\n',A+B)
print('A-B =\n',A-B)
#A*B#会报错，因为矩阵相乘必须满足A的行与B的列个数相等才行
'''
#三、Array的input和output
#使用pickle序列化numpy array
import pickle
import numpy as np
x = np.arange(10)
#f = open('x.pkl', 'wb')#打开文件操作，和py并无区别
#pickle.dump(x,f)#使用pickle把数组x给他dump到f中
#使用numpy序列化array到硬盘
#np.save('one_array', x)
#np.load('one_array.npy')
y = np.arange(20)
np.savez('two_array.npz',a=x,b=y)#通过numpy的savez把两个数组保存到一个npz压缩文件中，并取名为a,b
