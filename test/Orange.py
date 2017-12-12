# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:39:55 2017

@author: ms
"""
'''
if not isinstance(x,(int,float)):
    raise TypeError('bad operand type')
'''
import numpy as np

'''
def orange(data,rows=None,cols=None): 
    if rows == None and cols == None:
        for j in range(len(data)):
            if len(data)%(j+1) ==0:
                rows = (j+1)
                cols = int(len(data)/(j+1))
                if rows>=cols:
                    break
    elif rows == None :
        rows = int(len(data)/cols)
    elif cols == None:
        cols = int(len(data)/rows) 
    else:
        pass
        
    a = []
    for i in range(rows):
        a.append(np.hstack(data[i*cols : (i+1)*cols]))
    return np.vstack(a)
'''
def orange(*data):
    a = []
    for j in range(len(data)):
        a.append(np.hstack(data[j]))
    return np.vstack(a)

a1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
a2 = np.array([[2,2,2],[2,2,2],[2,2,2]])
b1 = np.array([[3,3,3],[3,3,3],[3,3,3]])
b2 = np.array([[4,4,4],[4,4,4],[4,4,4]])
c1 = np.array([[5,5,5],[5,5,5],[5,5,5]])
c2 = np.array([[6,6,6],[6,6,6],[6,6,6]])

data = ((a1,a2),(b1,b2),(c1,c2))
        
        
        
a = np.random.randint(10,size=9).reshape(3,3)
b = np.random.randint(10,size=9).reshape(3,3)
c = np.random.randint(10,size=9).reshape(3,3)
d = np.random.randint(10,size=9).reshape(3,3)
o = np.zeros((3,3))


