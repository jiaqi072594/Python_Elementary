# -*- coding: utf-8 -*-
#from dawn import *
import sys
import os
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf',size=14)
matplotlib.rcParams['axes.unicode_minus'] = False

data = open('C:\\Users\\ms\\Desktop\\twinCAT程序\\Sweep数据\\0911sweep数据\\PC 10 10.txt', mode='r', encoding='UTF-8')
a = data.read()
b = a.split('\n')
c = []

for i in range(len(b)):
    c.append( b[i].split('\t'))

for n in range(len(c[6])):
    if c[6][n] == 'iPos' :
        y_data = n
        x_data = n-1
        break
    
        
for n in range(21,len(c)):
    if int(c[n][y_data])>0 :
        start=n
        break
    

#生成测试数据
#x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#y_cos, y_sin = np.cos(x), np.sin(x)
x = []
y = []
for j in range(start,len(b)-3):
    x.append(int(c[j][x_data])-int(c[start][x_data]))
    y.append(int(c[j][y_data])*0.01)

#生成画布，并设定标题
plt.figure(figsize=(16,9), dpi=80)
plt.title(u'test', fontproperties=myfont)
plt.grid(True)

#设置X轴
plt.xlabel(u'X轴/ms', fontproperties=myfont)
plt.xlim(0, 6000)#设置X轴上下限
#plt.xticks(1)#设置横轴标记

#设置Y轴
plt.ylabel(u'Y轴/mm', fontproperties=myfont)
plt.ylim(0.0, max(y))
plt. yticks([0.0,max(y)*0.25,max(y)*0.5,max(y)*0.75,max(y)])

#画两条曲线
plt.plot(x,y, 'b-', linewidth=2.0, label=u'123')#绘制余弦曲线，蓝色，--，宽度为2的曲线
#plt.plot(x,y_sin, 'g-', linewidth=2.0, label=u'sin示例')#绘制余弦曲线，蓝色，-，宽度为2的曲线

#设置图例位置， loc可以为[upper, lower, left, right, center]
plt.legend(loc=u'upper left', prop=myfont, shadow=True)#
    
#以分辨率72来保存图片
#plt.savefig('test_save.png', dpi=72 )

#图形显示
plt.show()
