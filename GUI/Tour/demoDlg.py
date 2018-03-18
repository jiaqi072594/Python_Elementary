# -*- coding: utf-8 -*-
from tkinter import*            #获得基础组建集合
from dialogTable import demos   #按钮回调处理程序
from quitter import Quitter     #增加一个退出对象

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Basic demos').pack()
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__':
    Demo().mainloop()
