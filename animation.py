#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:47:29 2020

@author: lening
"""

import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))


# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
# a 潜伏者转化为感染者概率
#导入潜伏期人群（潜伏期具有传染性）
def SEIR_wuhan_blocked_model(N=10000, I= 1, r= 20, 
                             B= 0.03, r2= 20, 
                             B2= 0.03, y= 0.85, 
                             a= 0.1, bolckday= 25):

    #易感者
    S= N - I
    
    #复原者
    R= 0
    
    #潜伏者
    E= 0
    
    T = 199
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    Recovers= []
    Recovers.append(R)
    
    Exposed= []
    Exposed.append(E)
    
    for idx in range(T):
        if idx> bolckday:
            r= 5
            r2= 5
            
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N - r2*B2*Suspectors[idx]*Exposed[idx]/N)
        Exposed.append(Exposed[idx] + r*B*Suspectors[idx]*Infectors[idx]/N - a*Exposed[idx] + r2*B2*Suspectors[idx]*Exposed[idx]/N)
        Infectors.append(Infectors[idx] + a*Exposed[idx] - y*Infectors[idx])
        Recovers.append(Recovers[idx] + y*Infectors[idx])
    
    return Suspectors, Exposed, Recovers, Infectors

class UpdateDist(object):
    def __init__(self, ax):
        self.success = 0
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1000)
        self.ax.grid(True)

    def init(self):
        self.success = 0
        self.line.set_data([], [])
        return self.line,

    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            return self.init()
     
        Suspectors, Exposed, Recovers, Infectors = SEIR_wuhan_blocked_model(bolckday= 50 - i)
        
        self.line.set_data(self.x, Infectors)
        return self.line,

fig, ax = plt.subplots()
ud = UpdateDist(ax)
anim = FuncAnimation(fig, ud, frames= np.arange(120), init_func= ud.init,
                     interval= 50, blit= True)
anim.save('test_animation.gif', writer= 'imagemagick')
plt.show()
