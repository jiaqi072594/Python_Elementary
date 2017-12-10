# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:06:58 2017

@author: MOOM
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#plot的用法
'''
    a = [1,2,3]
    b = [4,5,6]
    c = [10,8,6]
    d = [1,8,3]
    
    #plt.plot(a)#Y轴坐标按照a的list X轴按照a的list的index
    #plt.plot(a,b)
    #plt.show()
    
    #魔法 %matplotlib inline
    #plt.plot(a,b,'r--',c,d,'b--')
    t = np.arange(0.0, 2.0, 0.1)#0-2之间的数字，每个数字之间间隔0.1
    s = np.sin(t*np.pi)
    #plt.plot(t,s,'r--',t*2,s,'--',t*3,s,'--')
    
    #加一个标签
    plt.xlabel('this is x')
    plt.ylabel('this is y')
    plt.title('this is a demo')
    
    #将line26信息补全
    plt.plot(t,s,'r--',label='aaa')
    plt.plot(t*2,s,'--',label='bbb')
    plt.plot(t*3,s,'--',label='ccc')
    plt.legend()#有了它能显示线的label
'''

#subplot的用法
#x = np.linspace(0.0, 5.0)
#y1 = np.sin(np.pi*x)
#y2 = np.sin(np.pi*x*2)
'''
#plt.subplot(2,1,1)#创建一个2*1的图表 在第一个
plt.subplot(2,2,1)#创建一个2*2的图表 在第一个
plt.plot(x,y1,'b--')
plt.ylabel('y1')
#plt.subplot(2,1,2)#再创建一个2*1的图表 在第二个
plt.subplot(2,2,2)#再创建一个2*2的图表 在第二个
plt.plot(x,y2,'r--')
plt.ylabel('y2')
plt.xlabel('x')
'''
'''
另一种用法
figure, ax = plt.subplots(2,2)
ax[0][0].plot(x,y1,'r')
ax[0][1].plot(x,y2,'b')
ax[1][0].plot(x,y1,'r--')
ax[1][1].plot(x,y2,'b--')
'''

#Pandas绘图之Series
'''
s1 = Series(np.random.randn(1000)).cumsum()#cumsum累计求和，比如a=[1,2,3,4,5],a.cunsum=[1,3,5,10,15]
s2 = Series(np.random.randn(1000)).cumsum()
#s1.plot(grid=True,label='S1',title='This is Series', style='--')#geid是现实标尺线，label是图例，title名称，style是线的类型
#s2.plot(grid=True,label='S2',title='This is Series', style='--')
plt.legend()

fig, ax = plt.subplots(2,2)
#ax[0].plot(s1)
#ax[1].plot(s2)

s1.plot(ax=ax[0][0],label='S1',title='this is Series',grid=True,style='r')
s2.plot(ax=ax[1][0],label='S2',grid=True)

#画成柱状图
s1[0:20].plot(ax=ax[0][1],kind='bar',label='s1',title='this is Series',grid=True)
s2[20:40].plot(ax=ax[1][1],label='s2',grid=True,style='r')
'''
 
#Pandas绘图之DataFrame
'''
df = DataFrame(
        np.random.randint(1,10,40).reshape(10,4),
        columns = ['a','b','c','d']
)
'''
#df.plot()#折现4组数据
#df.plot(kind='bar')#柱状图
#df.plot(kind='barh')#改变方向
#df.plot(kind='bar',stacked=True)#4列数据进行堆叠
#df.plot(kind='area')#填充
#选取某一行作图，比如第五行：
#a = df.iloc[5] 
#type(a)#pandas.core.series.Series
#a.plot()
'''
#每一行的数据展示到第一张图里面
for i in df.index:
    df.iloc[i].plot(label=str(i))
plt.legend()
'''
#上面用了循环，有更好的方式
#df.T.plot()#行列进行转制
#也可以
#df['a'].plot()

#直方图和密度图
s = Series(np.random.randn(1000))
#plt.hist(s, rwidth=0.9)#此图表示一种分布情况
#a = np.arange(10)
#plt.hist(a,rwidth=0.9)
#re = plt.hist(s, rwidth=0.9)
#type(re)#tuple
#len(re)#3 #re是一个tuple，有3个value，第一个是表示频率，也就是出现的次数，第二个就是取值间隔，第三个就是画出来的10个直方

#密度图
s.plot(kind='kde')#X轴是取值范围，y轴就是某个值出现的次数占到总数的百分比，比如0附近的取值占了总取值的40左右


