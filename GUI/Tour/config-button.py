# -*- coding: utf-8 -*-
from tkinter import*
widget = Button(text='Spam', padx=10, pady=10)              #设置留白
widget.pack(padx=20, pady=20)                               #设置留白
widget.config(cursor='hand2')                               #光标：cursor选项能够改变当鼠标经过组件时的鼠标指针的外观。gumby、watch、pencil、crdss、hand2等
widget.config(bd=8, relief=RAISED)                          #边框和浮凸：bd=8表示设置边框宽度为8，relief为指定一种边框类型FLAT(扁平)、SUNKEN(凹陷)、RAISED(凸起)、GROOVE(凹槽)、SOLTD(加粗)或RIDGE(脊状)
widget.config(bg='dark green', fg='white')                  
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()