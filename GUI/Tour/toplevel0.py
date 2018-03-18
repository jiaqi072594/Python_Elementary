# -*- coding: utf-8 -*-
import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()
win2 = Toplevel()
Button(win1, text='Spam', command=sys.exit).pack()#两个独立的窗口
Button(win2, text='SPAM', command=sys.exit).pack()#但是在同一个进程中

Label(text='Popups').pack() #默认的Tk()跟窗口，关闭则整个程序关闭
win1.mainloop()