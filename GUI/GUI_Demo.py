# -*- coding: utf-8 -*-

"""
import tkinter                         
widget = tkinter.Label(None, text='Hello GUI world!')   #生成 “None”表示“将新标签设置在该程序的默认顶层窗口”
widget.pack()                                   #布置
widget.mainloop()                               #开始事件循环
"""
"""
from tkinter import *
root = Tk()
Label(root, text='Hello GUI world!').pack(side=TOP)
root.mainloop()
"""
"""
from tkinter import *
Label(text='Hello GUI world!').pack(expand=YES, #expand=YES:要求打包几何管理器为组件扩展空间，通常可以是父组件中任何未被占用的difang
                                    fill=BOTH)#fill=BOTH：可以来拉升组件，使其充满分配的空间 也可以是Y或者X
mainloop()
"""
"""
#7-7 7-8
from tkinter import *
root = Tk()
widget = Label(root)
#widget['text'] = 'Hello GUI world!'
widget.config(text='Hello GUI world!')
#widget.pack(side=TOP)
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('gui1g.py')
root.mainloop()
"""
"""
#7-10
import sys
from tkinter import*
widget = Button(None, text='Hello GUI world!', command=sys.exit)
widget.pack()
widget.mainloop()
"""
"""
#7-11
from tkinter import*
root = Tk()
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X)
root.mainloop()
"""
"""
#7-12
import sys 
from tkinter import*

def quit():
    print('Hello, I must be going...')
    sys.exit()
widget = Button(None, text='Hello GUI world!', command=quit)
widget.pack()
widget.mainloop()
"""
"""
#7-13
import sys 
from tkinter import*

widget = Button(None,
            text='Hello GUI world!',
            command=(lambda: print('Hello lambda world' )or sys.exit()) )
widget.pack()
widget.mainloop()
"""
"""
#7-14
import sys
from tkinter import*

class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello GUI world', command=self.quit)
        widget.pack()
    def quit(self):
        print('Hello class method world')
        sys.exit()

HelloClass()
mainloop()
"""
"""
#7-15
import sys 
from tkinter import*

class HelloCallable:
    def __init__(self):
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)
        sys.exit()

widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()
"""
"""
#7-16
import sys
from tkinter import*

def hello(event):
    print('Pree twice to exit')

def quit(event):
    print('Hello, I must be going...')
    sys.exit()

widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)    #绑定单机鼠标左键
widget.bind('<Double-1>', quit)     #绑定双击鼠标左键
widget.mainloop()
"""
"""
#7-17
from tkinter import*

def greeting():
    print('Hello stdout world!...')
win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='quit', command=win.quit).pack(side=RIGHT)
win.mainloop()
"""
"""
#7-18
from tkinter import*

class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)
    def callback(self):
        print('Goodbye world...')
        self.quit()

if __name__=='__main__':
    HelloButton(text='Hello subclass world').mainloop()
"""
"""
#7-19
from tkinter import*
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)
    def callback(self):
        print('Goodbye world...')
        self.quit()
class MyButton(HelloButton):
    def callback(self):
        print('Ignoring press!...')

if __name__=='__main__':
    MyButton(None, text='Hello subclass world').mainloop()
"""
"""
#7-20
from tkinter import*

class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)
    
    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)

if __name__ == '__main__':
    Hello().mainloop()
"""
"""
#7-21
from sys import exit
from tkinter import *

class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)
    
    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)

parent = Frame(None)    #生成一个容器组件
parent.pack()
Hello(parent).pack(side=RIGHT)  #附件Hello而不运行
Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
"""
"""
#7-23
from tkinter import *
class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)
    
    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)
class HelloExtender(Hello): #拓展了方法
    def make_widgets(self):
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):  #重新定义的方法
        print('Hello', self.data)

if __name__ == '__main__':
    HelloExtender().mainloop()
"""
"""
#7-24 gui7
from tkinter import *

class HelloPackage:                 #不是组件的子类
    def __init__(self, parent=None):   
        self.top = Frame(parent)    #嵌入框架
        self.top.pack()
        self.data = 0
        self.make_widgets()         #将组件附加到self.top
    
    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)
    
    def message(self):
        self.data +=1
        print('Hello number', self.data)

if __name__ == '__main__':
    HelloPackage().top.mainloop()
"""
"""
#7-26 
from tkinter import *
import gui7

class HelloPackage(gui7.HelloPackage):
    def __getattr__(self, name):
        return getattr(self.top, name)  #完成并传递到一个实际组件

if __name__ == '__main__':
    HelloPackage().mainloop()           #触发__getattr__
"""

'''

组件类                                   描述
Label                               一块简单消息区域
Button                              一个简单带标签的按钮组件
Frame                               用于盛放和布置其他组件对象
Toplevel, TK                        由窗口管理器管理的新窗口    
Message                             一个多行标签
Entry                               一个简单单行文本输入区域
Checkbutton                         双状态的按钮组件、尤用于多项选择
Radiobutton                         双状态的按钮组件、尤用于单项选择
Scale                               可衡量位置的滑动组件
PhotoImage                          图像组件，用于在其他组件上显示全彩色图像
BitmapImage                         图像组件，用于在其他组件上显示位图
Menu                                与菜单按钮或顶层窗口相关的一组选项
Menubutton                          打开菜单按钮选项和子菜单的按钮
Scrolbar                            滚动其他组件的组件的控件（如列表框、画布、文本框）
Lisbox                              选项的列表
Text                                多行文本浏览/编辑组件，支持文字体
Canvas                              图形绘画区域，支持线条、圆圈、照片、文本等

集合管理器：pack, grid, place
tkinter连接变量：StringVar. InVar, DoubleVar, BooleanVar
高级TK组件：Spinbox, LabelFrame, PanedWindow
复合组件：Dialog, ScrolledText, OptionMenu
回调安排：组件的after, wait, update方法
其他工具：标准对话框，剪切板，bind和Event，组件设置选项，用户对话框，模式对话框，动画技巧

'''