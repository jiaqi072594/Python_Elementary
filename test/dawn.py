# -*- coding: utf-8 -*-
#from dawn import *
import sys
import os
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf',size=14)
matplotlib.rcParams['axes.unicode_minus'] = False

#data = open('C:\\Users\\ms\\Desktop\\twinCAT程序\\Sweep2.5\\data\\cyc325.txt', mode='r', encoding='UTF-8')
#a = data.read()
#b = a.split('\n')#b[]表示行
file = 'cyc325'
b = open('C:\\Users\\ms\\Desktop\\twinCAT程序\\Sweep2.5\\data\\'+file+'.txt', mode='r', encoding='UTF-8').read().split('\n')
c = []#c[][]第一个是行 第二个是列

for i in range(len(b)):
    c.append( b[i].split('\t'))

for n in range(len(c[6])):
    if c[6][n] == 'iPos' :
        y_data = n
        x_data = n-1
        break
for n in range(len(c[6])):
    if c[6][n] == 'bSweepOn' :
        SweepOn = n
        break
for n in range(21,len(c)):
    if int(c[n][SweepOn])==1 :
        start=n
        break
for n in range(start,len(c)):
    if int(c[n][SweepOn])==0 :
        end=n
        break
    
'''        
for n in range(21,len(c)):
    if int(c[n][y_data])>0 :
        start=n
        break
'''  

#生成测试数据
#x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#y_cos, y_sin = np.cos(x), np.sin(x)
x = []
y = []
for j in range(start,len(b)-3):#len(b)-3
    x.append((int(c[j][x_data])-int(c[start][x_data]))*0.001)
    #print(c[j][x_data])
   # print(j)
    y.append(int(c[j][y_data])*0.01)

#生成画布，并设定标题
plt.figure(figsize=(16,9), dpi=75)#resolution= figsize*dpi
#plt.title(u'test', fontproperties=myfont,loc=u'right')
#plt.grid(True)#网络格
ax = plt.gca()#刚擦： get current axis

#设置X轴
plt.xlabel(u'X轴/s', fontproperties=myfont)
plt.xlim(0, 24)#设置X轴上下限
#plt.xticks([0.0,3.0,6.0,9.0,12.0,15.0,18.0,21.0,24.0])#设置横轴标记
plt.xticks(np.linspace(0, 24, 25, endpoint=True))

#设置Y轴
plt.ylabel(u'Y轴/mm', fontproperties=myfont)
plt.ylim(0.0, max(y)+100)
plt. yticks([0.0,max(y)*0.25,max(y)*0.5,max(y)*0.75,max(y),max(y)*1.25])

#画两条曲线
plt.plot(x,y, 'b-', linewidth=2.0, label=file)#绘制余弦曲线，蓝色，--，宽度为2的曲线
#plt.plot(x,y_sin, 'g-', linewidth=2.0, label=u'sin示例')#绘制余弦曲线，蓝色，-，宽度为2的曲线

#设置图例位置， loc可以为[upper, lower, left, right, center]
plt.legend(loc=u'upper left', prop=myfont, shadow=True)#
  
#移动坐标轴到原点
#先将上方和右方的spine去掉（color设置为none即可）
#再将x(y)坐标轴设为下方（左方）的spine，并且移动到原点
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


#标注（annotate）
#在X=t处画虚线，并且把（他，一）这个用plt.scatter的方式标记出来
#在（t，y）处用plt.annotate方法以箭头的方式做标注

t = x[end-start]
plt.plot([t,t],[0,y[end-start]],color='blue',linewidth=1,linestyle='--')
plt.scatter([t],y[end-start],50,color='red')
plt.annotate(r'SweepOn=False',xy=(t,y[-1]),xycoords='data',
             xytext=(10,30),textcoords='offset points',
             fontsize=11,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

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
#plt.savefig('cyc325.png', dpi=80 )
