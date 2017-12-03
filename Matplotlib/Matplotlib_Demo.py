# -*- coding: utf-8 -*
#import matplotlib
#导入pyplot包，并简写为plt
import matplotlib.pyplot as plt
#定义2个点的x集合和y集合
x=[1,2]
y=[2,4]
#画散点图

#调整点的颜色为红色，调整点的形状为x，调整点的大小为30
plt.scatter(x,y,c='red',marker=(6,1),s=30)
'''
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, 
    cmap=None, norm=None, vmin=None, vmax=None, alpha=None, 
    linewidths=None, verts=None, edgecolors=None, hold=None, 
    data=None, **kwargs)
Returns: paths : PathCollection

x, y : array_like,shape (n, )
    Input data

s : scalar or array_like, shape (n, ), optional
    size in points^2. Default is rcParams
    ['lines.markersize'] ** 2.

c : color, sequence, or sequence of color, optional, default: ‘b’
      c can be a single color format string, or a sequence of 
    color specifications of length N, or a sequence of N numbers 
    to be mapped to colors using the cmap and norm specified via 
    kwargs (see below). Note that c should not be a single numeric 
    RGB or RGBA sequence because that is indistinguishable from an 
    array of values to be colormapped. c can be a 2-D array in which
    the rows are RGB or RGBA, however, including the case of a single 
    row to specify the same color for all points.

marker : MarkerStyle, optional, default: ‘o’
      See markers for more information on the different styles of 
    markers scatter supports. marker can be either an instance of 
    the class or the text shorthand for a particular marker.

cmap : Colormap, optional, default: None
      A Colormap instance or registered name. cmap is only used if 
    c is an array of floats. If None, defaults to rc image.cmap.

norm : Normalize, optional, default: None
      A Normalize instance is used to scale luminance data to 0, 1. 
    norm is only used if c is an array of floats. If None, use the 
    default normalize().

vmin, vmax : scalar, optional, default: None
      vmin and vmax are used in conjunction with norm to normalize 
    luminance data. If either are None, the min and max of the color
    array is used. Note if you pass a norm instance, your settings 
    for vmin and vmax will be ignored.

alpha : scalar, optional, default: None
      The alpha blending value, between 0 (transparent) and 1 (opaque)

linewidths : scalar or array_like, optional, default: None
      If None, defaults to (lines.linewidth,).

verts : sequence of (x, y), optional
      If marker is None, these vertices will be used to construct the 
    marker. The center of the marker is located at (0,0) in normalized 
    units. The overall marker is rescaled by s.

edgecolors : color or sequence of color, optional, default: None
      If None, defaults to ‘face’

      If ‘face’, the edge color will always be the same as the face color.

      If it is ‘none’, the patch boundary will not be drawn.

      For non-filled markers, the edgecolors kwarg is ignored and forced 
    to ‘face’ internally.

**kwargs : Collection properties

'''
#[]里的4个参数分别表示X轴起始点，X轴结束点，Y轴起始点，Y轴结束点
plt.axis([0,10,0,10])
#展示绘画框
plt.show()