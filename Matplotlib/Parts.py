# -*- coding: utf-8 -*
'''
1.简单的折线图
2.Y轴范围不一致的折线图
3.子图的画法
4.简单的柱状图
5.水平方向的柱状图
6.更高级的柱状图
7.类表格图形
8.直方图
9.饼图
10.散点图
11.雷达图
12.三维散点图
13.三维折线图
14.三维柱状图
15.图形填充

'''
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.font_manager as fm 
# from mpl_toolkits.molot3d import Axes3Dr

# 解决中文乱码问题
#myfont = fm.FontProperties(fname='/Librart/Fonts/Songti.ttc',size=14)

myfont = fm.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf',size=14)
matplotlib.rcParams['axes.unicode_minus'] = False

def simple_plot():
    '''
    simple plot
    '''
    #生成测试数据
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)

    #生成画布，并设定标题
    plt.figure(figsize=(8,6), dpi=80)#创建一个8*6点（point）的图，并设置分辨率为80
    plt.title(u'简单的曲线图', fontproperties=myfont)
   plt.

    #设置X轴
    plt.xlabel(u'X轴', fontproperties=myfont)
    plt.xlim(-4.0, 4.0)#设置X轴上下限
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))#设置横轴标记

    #设置Y轴
    plt.ylabel(u'Y轴', fontproperties=myfont)
    plt.ylim(-1.0, 1.0)
    plt. yticks(np.linspace(-1, 1, 9, endpoint=True))

    #画两条曲线
    plt.plot(x,y_cos, 'b--', linewidth=2.0, label=u'cos示例')#绘制余弦曲线，蓝色，--，宽度为2的曲线
    plt.plot(x,y_sin, 'g-', linewidth=2.0, label=u'sin示例')#绘制余弦曲线，蓝色，-，宽度为2的曲线

    #设置图例位置， loc可以为[upper, lower, left, right, center]
    plt.legend(loc=u'upper left', prop=myfont, shadow=True)#
    
    #以分辨率72来保存图片
    #plt.savefig('test_save.png', dpi=72 )

    #图形显示
    plt.show()
    return
simple_plot()

def simple_advanced_plot():
    '''
    simple advanced plot
    '''
    #生成测试数据
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)

    #生成画布，并设定标题
    plt.figure(figsize=(8, 6), dpi=80 )
    plt.title('复杂曲线图', fontproperties=myfont)
    plt.grid(True)

    #画图的另外一种方式
    ax_1 = plt.subplot(111)#subplot(1,1,1) 创建一个新的1*1的子图，接下来的图样绘制在其中的第一块（也是唯一的一块）
    ax_1.plot(x, y_cos, color='blue', linewidth=2.0, linestyle='--', label='左cos')
    ax_1.legend(loc='upper left', prop=myfont, shadow=True)

    #设置Y轴（左边）
    ax_1.set_ylabel('左cos的y轴',fontproperties=myfont)
    ax_1.set_ylim(-1.0, 1.0)
    ax_1.set_yticks(np.linspace(-1, 1, 9, endpoint=True))

    #画图的另外一种方式
    ax_2 = ax_1.twinx()
    ax_2.plot(x,y_sin,color='green', linewidth=2.0, linestyle='-',label='右sin')
    ax_2.legend(loc='upper right', prop=myfont, shadow=True)

    #设置Y轴（右边）
    ax_2.set_ylabel('右sin的y轴',fontproperties=myfont)
    ax_2.set_ylim(-2.0, 2.0)
    ax_2.set_yticks(np.linspace(-2, 2, 9, endpoint=True))

    #设置X轴（共同）
    ax_1.set_xlabel('x轴', fontproperties=myfont)
    ax_1.set_xlim(-4.0, 4.0)
    ax_1.set_xticks(np.linspace(-4,4,9,endpoint=True))

    #图形显示
    plt.show()
    return
#simple_advanced_plot()

def subplot_plot():
    '''
    subplot plot
    '''
    #子图的style列表
    style_list = ['g+-', 'r*-', 'b.-', 'yo-']

    #依次画图
    for num in range(4):
        #生成测试数据
        x = np.linspace(0.0, 2+num, num=10*(num+1))
        y = np.sin((5-num)*np.pi*x)
        
        #子图的生成方式
        plt.subplot(2, 2, num+1)
        plt.title('子图 %d' %(num+1), fontproperties=myfont)
        plt.plot(x, y, style_list[num])

    #图形显示
    plt.show()
    return
#subplot_plot()

def bar_plot():
    '''
    bar plot
    '''
    #生成测试数据
    #设置标题
    #画柱状图
    #设置柱状图标示
    #设置刻度范围/坐标轴名称等
    #图形显示
    plt.show()
    return
#bar_plot()

def bar_advanced_plot():
    '''
    bar_advanced plot
    '''
    #生成测试数据
    #设置标题
    #设置相关参数
    #画柱状图（两种：X轴以上/X轴以下）
    #画折线图（两种，和柱状图对应）
    #设置圆形标示（两种，和柱状图对应）
    #设置Y轴和图例位置
    #图形显示
    plt.show()
    return
#bar_advanced_plot()

def table_plot():
    '''
    table plot
    '''
    #生成测试数据
    #设置标题
    #设置相关参数
    #声明底部位置
    #依次画图，并更新底部位置
    #设置图例位置
    #图形显示
    plt.show()
    return
#table_plot()

def histograms_plot():
    '''
    histograns plot
    '''
    #生成测试数据
    #设置标题
    #画直方图，并返回相关结果
    #根据直方图返回的结果，画折线图
    #设置图例位置
    #图形显示
    plt.show()
    return
#histograms_plot()

def pie_plot():
    '''
    pie plot
    '''
    #生成测试数据
    #设置标题
    #设置突出参数
    #画饼状图
    #图形显示
    plt.show()
    return
#pie_plot()

def scatter_plot():
    '''
    scatter plot
    '''
    #生成测试数据
    #设置标题
    #设置相关参数
    #画散点图
    #图形显示
    plt.show()
    return
#scatter_plot()

def fill_plot():
    '''
    fill plot
    '''
    #生成测试数据
    #设置标题
    #画图
    #填充图形
    #图形显示
    plt.show()
    return
#fill_plot()

def radar_plot():
    '''
    radar plot
    '''
    #生成测试数据
    #数据预处理
    #画图方式
    #设置"theta grid"/"radar grid"
    #画雷达图，并填充雷达图内部区域
    #图形显示
    plt.show()
    return
#radar_plot()

def three_dimension_scatter():
    '''
    3d scatter plot
    '''
    #生成测试数据
    #生成画布（两种形式）
    #画三维散点图
    #设置坐标轴范围
    #图形显示
    plt.show()
    return
#three_dimension_scatter()

def three_dimension_line():
    '''
    3d line plot
    '''
    #生成测试数据
    #生成画布（两种形式）
    #画三维折线图
    #设置坐标轴图标
    #图形显示
    plt.show()
    return
#three_dimension_line()

def three_dimension_bar():
    '''
    3d bar plot
    '''
    #生成测试数据（位置数据）
    #生成测试数据（柱形参数）
    #生成画布（两种形式）
    #画三维柱状图
    #设置坐标轴图标
    #图形显示
    plt.show()
    return
#three_dimension_bar