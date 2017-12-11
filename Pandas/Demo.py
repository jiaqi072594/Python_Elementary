# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:35:01 2017

@author: ms
"""
'''
结构化数据分析利器（依赖numpy）
提供了多种高级数据结构
将大的数据索引和处理能力
'''
'''
1.Series
2.DataFrame
3.输入理解Deries和DataFrame
4.Pandas的IO操作
5.DataFrame的Selecting和indexing
6.Reindexing Series and DataFrame
7.关于NaN
8.多级index
9.Mapping and Replace 
'''
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
'''
#1.Series 定长，有序的字典
s1 = pd.Series([1,2,3,4])#创建series
s1.values#查看series的值
s1.index#查看series的索引
s2 = pd.Series(np.arange(10))#创建一个长度为10的series
s3 = pd.Series({'1':1,'2':2,'3':3})#通过py字典创建Series
s4 = pd.Series([1,2,3,4], index=['a','b','c','d'])#创建series并设置索引index
s4['a']#查询series中的值
s4[s4>2]#按条件查询series中的值
s4.to_dict()#把series转换成dict
s5 = pd.Series(s4.to_dict())

#索引超出数据范围情况下的显示
index_1 = ['a','b','c','d','e']
s6 = pd.Series(s5,index=index_1)
pd.isnull(s6)#找出为NaN的数据位置
pd.notnull(s6)#找出不为NaN的位置
s6.name = 'demo'
s6.index.name = 'demo index'#3给series的索引起名字
'''

#2.DataFrame






























































































































































































