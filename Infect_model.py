# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:37:50 2020
Infection model
By referring following URL:
https://zhuanlan.zhihu.com/p/104268573?night=1
@author: LENING
"""

import pylab as pl

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
def SI_model(N= 10000, I= 1, r= 10, B= 0.01):

    #易感者
    S= N - I
    T = 200
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    for idx in range(T):
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N)
        Infectors.append(Infectors[idx] + r*B*Infectors[idx]*Suspectors[idx]/N)
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Infectors, label= u"Infectors")
    pl.legend()
    pl.show()

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
#康复者将有可能再次感染
def SIS_model(N= 10000, I= 1, r= 10, B= 0.01, y= 0.02):

    #易感者
    S= N - I
    T = 200
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    for idx in range(T):
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N + y*Infectors[idx])
        Infectors.append(Infectors[idx] + r*B*Infectors[idx]*Suspectors[idx]/N - y*Infectors[idx])
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Infectors, label= u"Infectors")
    pl.legend()
    pl.show()

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
# 康复者将具有抗体不再感染    
def SIR_model(N= 10000, I= 1, r= 10, B= 0.05, y= 0.1):

    #易感者
    S= N - I
    
    #复原者
    R= 0
    
    T = 200
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    Recovers= []
    Recovers.append(R)
    
    for idx in range(T):
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N)
        Infectors.append(Infectors[idx] + r*B*Infectors[idx]*Suspectors[idx]/N - y*Infectors[idx])
        Recovers.append(Recovers[idx] + y*Infectors[idx])
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Infectors, label= u"Infectors")
    pl.plot(Recovers, label= u"Recovers")
    pl.legend()
    pl.show()

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
# a 潜伏者转化为感染者概率
#导入潜伏期人群(潜伏期不具有传染性)
def SEIR_model(N= 10000, I= 1, r= 20, B= 0.03, y= 0.1, a= 0.1):

    #易感者
    S= N - I
    
    #复原者
    R= 0
    
    #潜伏者
    E= 0
    
    T = 200
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    Recovers= []
    Recovers.append(R)
    
    Exposed= []
    Exposed.append(E)
    
    for idx in range(T):
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N)
        Exposed.append(Exposed[idx] + r*B*Suspectors[idx]*Infectors[idx]/N-a*Exposed[idx])
        Infectors.append(Infectors[idx] + a*Exposed[idx] - y*Infectors[idx])
        Recovers.append(Recovers[idx] + y*Infectors[idx])
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Exposed, label= u"Exposed")    
    pl.plot(Infectors, label= u"Infectors")
    pl.plot(Recovers, label= u"Recovers")

    pl.legend()
    pl.show()

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
# a 潜伏者转化为感染者概率
#导入潜伏期人群（潜伏期具有传染性）
def SEIR_wuhan_model(N= 10000, I= 1, r= 20, B= 0.03, r2= 20, B2= 0.03, y= 0.1, a= 0.1):

    #易感者
    S= N - I
    
    #复原者
    R= 0
    
    #潜伏者
    E= 0
    
    T = 200
    
    Infectors= []
    Infectors.append(I)
    
    Suspectors= [] 
    Suspectors.append(S)
    
    Recovers= []
    Recovers.append(R)
    
    Exposed= []
    Exposed.append(E)
    
    for idx in range(T):
        Suspectors.append(Suspectors[idx] - r*B*Infectors[idx]*Suspectors[idx]/N - r2*B2*Suspectors[idx]*Exposed[idx]/N)
        Exposed.append(Exposed[idx] + r*B*Suspectors[idx]*Infectors[idx]/N - a*Exposed[idx] + r2*B2*Suspectors[idx]*Exposed[idx]/N)
        Infectors.append(Infectors[idx] + a*Exposed[idx] - y*Infectors[idx])
        Recovers.append(Recovers[idx] + y*Infectors[idx])
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Exposed, label= u"Exposed")    
    pl.plot(Infectors, label= u"Infectors")
    pl.plot(Recovers, label= u"Recovers")

    pl.legend()
    pl.show()

# N 人口总数
# I 感染者
# r 感染者接触易感者的人数
# B 传染概率
# y 康复概率
# a 潜伏者转化为感染者概率
#导入潜伏期人群（潜伏期具有传染性）
def SEIR_wuhan_blocked_model(N= 10000, I= 1, r= 20, B= 0.03, r2= 20, B2= 0.03, y= 0.1, a= 0.1, bolckday= 10):

    #易感者
    S= N - I
    
    #复原者
    R= 0
    
    #潜伏者
    E= 0
    
    T = 200
    
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
    
    pl.plot(Suspectors,  label= u"Susceptibles")
    pl.plot(Exposed, label= u"Exposed")    
    pl.plot(Infectors, label= u"Infectors")
    pl.plot(Recovers, label= u"Recovers")

    pl.legend()
    pl.show()
    return max(Infectors), Infectors.index(max(Infectors))

if __name__ == '__main__':
    #SI_model()
    #SIS_model()
    #SIR_model()
    #SEIR_model()
    #SEIR_wuhan_model()
    
    for i in range(30):
        print(i, SEIR_wuhan_blocked_model(bolckday= i))