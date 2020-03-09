# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:08:14 2020

@author: leoring_le@hotmail.com
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func2(x, p):
    """
    数据拟合所用的函数: k*x+b
    """
    a, b, c = p
    return a*x*x + b*x + c

def func3(x, p):
    """
    数据拟合所用的函数: k*x+b
    """
    a, b, c, d = p
    return a*x*x*x + b*x*x + c*x + d

def func4(x, p):
    """
    数据拟合所用的函数: k*x+b
    """
    a, b, c, d, e = p
    return a*x*x*x*x + b*x*x*x + c*x*x + d*x + e

def residuals(p, y, x, func= func4):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

def SSE(p,y,x,func):
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
    
    # 第一次猜测的函数拟合参数
    func = func4
    if func == func4:
        p0 = [1, 1, 1, 1, 1]
    elif func == func3:
        p0 = [1, 1, 1, 1] 
    else:
        p0 = [1, 1, 1] 
        
    # 调用leastsq进行数据拟合
    # residuals为计算误差的函数
    # p0为拟合参数的初始值
    # args为需要拟合的实验数据
    plsq = leastsq(residuals, p0, args=(y, x))

    print (u"拟合参数", plsq[0]) # 实验数据拟合后的参数
    print(u"R方", 1-SSE(plsq[0],y,x, func)/SST(y))

    pl.plot(x, y, label= "Data with Noise")
    pl.plot(x, func(x, plsq[0]), label= "Fitted Value")
    pl.legend()
    pl.show()

if __name__ == '__main__':
    main()
