# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:45:37 2017

@author: MOOM
"""

import sys
import os
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.font_manager as fm

'''
定义一个函数
输入：path
处理：
输出：一个二维度列表，内容为X轴坐标和Y轴坐标
'''

def get_data(path,data_name,row_mark='\n',col_mark='\t'):
    if path[-3:] == 'txt':
        data = []
        data_rows = open(path, mode='r', encoding='UTF-8').read().split(row_mark)
        for i in range(len(data_rows)):
            data.append(data_rows[i].split(col_mark))
        y_title = data[6].index(data_name)
        start = 21
        end = data.index(['EOF'])-1
        x_data = []
        y_data = []
        for i in range(start,end):
            x_data.append(eval(data[i][y_title-1]))
            y_data.append(eval(data[i][y_title]))
        return [x_data,y_data]
    else:
        print(u'请输入txt文件')
       
def dawn_data(data):
    myfont = fm.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf',size=14)
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(16,9), dpi=75)
    ax = plt.gca()
    plt.xlabel(u'X轴/s', fontproperties=myfont)
    plt.xlim(0, data[0][-1])#设置X轴上下限
    #plt.xticks(np.linspace(0, 24, 25, endpoint=True))
    plt.ylabel(u'Y轴/mm', fontproperties=myfont)
    plt.ylim(0.0, max(data[1])+100)
    plt. yticks([0.0,max(data[1])*0.25,max(data[1])*0.5,max(data[1])*0.75,max(data[1]),max(data[1])*1.25])
    
    plt.plot(data[0],data[1], 'b-', linewidth=2.0, label='test')
    plt.legend(loc=u'upper left', prop=myfont, shadow=True)#
    
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    #标注（annotate）
    #在X=t处画虚线，并且把（他，一）这个用plt.scatter的方式标记出来
    #在（t，y）处用plt.annotate方法以箭头的方式做标注
    '''
    t = x[end-start]
    plt.plot([t,t],[0,y[end-start]],color='blue',linewidth=1,linestyle='--')
    plt.scatter([t],y[end-start],50,color='red')
    plt.annotate(r'SweepOn=False',xy=(t,y[-1]),xycoords='data',
                 xytext=(10,30),textcoords='offset points',
                 fontsize=11,
                 arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
    '''
    #标注（text）#verticalalignment=('top', 'bottom', 'center', 'baseline')
    '''
    plt.text(-2,0.8,'1234567',verticalalignment='bottom',
             horizontalalignment='right',color='green',
             fontsize=8,bbox={'facecolor':'red','alpha':0.4,'pad':2})
    '''  
    #以分辨率72来保存图片
    #plt.savefig('test_save.png', dpi=72 )
    
    #图形显示
    plt.show()
    return
     
     
      
if __name__=="__main__":
    path = 'I:\\临时\\1214test\\cyc325.txt'
    data_name = 'iPos'
    data = get_data(path,data_name)
    dawn_data(data)