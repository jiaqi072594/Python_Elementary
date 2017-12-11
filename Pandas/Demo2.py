# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:47:02 2017

@author: ms
"""

'''
数据分箱
数据分组
数据聚合
透视表
'''
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
'''
#1.数据分箱
score_list = np.random.randint(30,100,size=20)#创建一个长度为20 范围在30-100之间的学生分组的数组
bins = [0,59,70,80,100]#设置一个分箱 表示数据有0-59 59-70 70-80 80-100这几个等级
score_cat = pd.cut(score_list, bins)#将分箱和分数利用cut方法结合到一起
pd.value_counts(score_cat)
#下面创建一个DataFrame，把数据放进去，再随机生成字符串表示学生姓名。
df = DataFrame()
df['score'] = score_list
df['student'] = [pd.util.testing.rands(3) for i in range(20)]
df['Categories'] = pd.cut(df['score'],bins,labels=['Low','OK','Good','Great'])
print(df)
'''
#2.数据分组
df = pd.read_excel('C:\\Users\\ms\\Desktop\\twinCAT程序\\Sweep数据\\Headsweep 50.xlsx')
