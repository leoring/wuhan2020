# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:08:14 2020
@author: leoring_le@hotmail.com
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    """
    数据拟合所用的函数: k*x+b
    """
    b, k = p
    return k*x+b

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

def SSE(p,y,x):
    sse = 0
    
    xlen = len(x)
    for i in range(xlen):
        sse += (y[i] - func(x[i],p))*(y[i] - func(x[i],p))
    return sse
    
def SST(y):
    sst = 0
    
    average = np.mean(y)
    for item in y:
        sst += (item - average) * (item - average)
    return sst 

def main():
    x= [1,2,3,4,
        5,6,7,8,9,
        10,11,12,13,
        14,15,16,17,
        18,19,20]

    y= [27,26,393,1118,1309,3806,
        2077,3248,4148,4812,5019,
        4562,5173,5072,3971,5328,
        4833,4214,3916,4008]

    x = np.array(x)
    y = np.array(y)
     
    p0 = [1, 1] # 第一次猜测的函数拟合参数

    # 调用leastsq进行数据拟合
    # residuals为计算误差的函数
    # p0为拟合参数的初始值
    # args为需要拟合的实验数据
    plsq = leastsq(residuals, p0, args=(y, x))

    #print (u"真实参数:", [b, k]) 
    print (u"拟合参数", plsq[0]) # 实验数据拟合后的参数
    print(u"R方", 1-SSE(plsq[0],y,x)/SST(y))

    pl.plot(x, y, label= "Original Data")
    pl.plot(x, func(x, plsq[0]), label= "Fitted Value")
    pl.legend()
    pl.show()

if __name__ == '__main__':
    main()
