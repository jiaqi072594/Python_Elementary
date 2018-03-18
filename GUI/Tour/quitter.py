# -*- coding: utf-8 -*-
"""
验证退出请求的Quit按钮
复用、连接其他GUI的实例，并按需求重新封装
"""

from tkinter import*                            #获取组件的类
from tkinter.messagebox import askokcancel      #获取封装的标准对话框

class Quitter(Frame):                           #GUI子类
    def __init__(self, parent=None):            #构造方法
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans:
            Frame.quit(self)

if __name__ == '__main__':
    Quitter().mainloop()