'''
    利用shelve模块，可以讲Python程序中的变量保存到二进制的shelf文件中。程序就可以从硬盘中恢复变量的数据。
    调用函数shelve.open()并传入一个文件名，然后将返回的值保存在一个变量中。可以对这个变量的shelf值进行修改，就像她是一个字典一样。当你完成是，在这个值上调用close（
。shelf值保存在shelfFile中。
'''

import shelve
