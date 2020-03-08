# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:37:50 2020
Infection model
By referring following URL:
https://zhuanlan.zhihu.com/p/104268573?night=1
@author: leoring_le@hotmail.com
"""

import matplotlib.pyplot as plt
import random

class infection_model():
    def __init__(self, 
                 population= 10000,
                 infectors_num= 1,
                 contactors_num= 10,
                 infect_prob= 0.05):
        
        super(infection_model, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.contactors_num = contactors_num
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
            
    def getIntervalValue(self):
        return self.interval

    def getMaxInfectors(self):
        return max(self.infectors), self.infectors.index(max(self.infectors))
 

# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数
# infect_prob 传染概率
class SI(infection_model):
    def __init__(self, 
                 population= 10000,
                 infectors_num= 1,
                 contactors_num= 10,
                 infect_prob= 0.05):
        
        super(SI, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.contactors_num = contactors_num
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
            
    def update(self):
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]* self.suspectors[-1]/self.population)
        self.infectors.append(self.infectors[-1] + self.contactors_num*self.infect_prob*self.infectors[-1]* self.suspectors[-1]/self.population)

        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        
        plt.legend()
        plt.show()

# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数
# infect_prob 传染概率
# recover_prob 康复概率
# 康复者将具有抗体不再感染    
class SIR(infection_model):
    def __init__(self, 
                 population= 10000,
                 infectors_num= 1,
                 contactors_num= 10, 
                 infect_prob= 0.05,
                 recover_prob= 0.1):
        
        super(SIR, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
                
        recovers= []
        recovers.append(0)
        self.recovers = recovers        
            
    def update(self):
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]* self.suspectors[-1]/self.population)
        self.infectors.append(self.infectors[-1] + self.contactors_num*self.infect_prob*self.infectors[-1]* self.suspectors[-1]/self.population - self.recover_prob*self.infectors[-1])
        self.recovers.append(self.recovers[-1] + self.recover_prob*self.infectors[-1])        
        
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        plt.plot(self.recovers, label= u"Recovers")
        
        plt.legend()
        plt.show()
    
# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数
# infect_prob 传染概率
#  recover_prob 康复概率
# 康复者将有可能再次感染
class SIS(infection_model):
    def __init__(self, 
                 population= 10000, 
                 infectors_num= 1,
                 contactors_num= 10, 
                 infect_prob= 0.05,
                 recover_prob= 0.02):
        
        super(SIS, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
            
    def update(self):
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population + self.recover_prob*self.infectors[-1])
        self.infectors.append(self.infectors[-1] + self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population - self.recover_prob*self.infectors[-1])
        
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        
        plt.legend()
        plt.show()        
        
# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数
# infect_prob 传染概率
# recover_prob 康复概率
# alpha_prob 潜伏者转化为感染者概率
#导入潜伏期人群(潜伏期不具有传染性)
class SEIR(infection_model):
    def __init__(self, 
                 population= 10000, 
                 infectors_num= 1, 
                 contactors_num= 10, 
                 infect_prob= 0.05, 
                 recover_prob= 0.1, 
                 alpha_prob= 0.9):
        
        super(SEIR, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.alpha_prob = alpha_prob
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
    
        recovers= []
        recovers.append(0)
        self.recovers = recovers     
        
        exposed= []
        exposed.append(0)
        self.exposed= exposed
            
    def update(self):
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population)
        self.exposed.append(self.exposed[-1] + self.contactors_num*self.infect_prob*self.suspectors[-1]*self.infectors[-1]/self.population-self.alpha_prob*self.exposed[-1])
        self.infectors.append(self.infectors[-1] + self.alpha_prob*self.exposed[-1] - self.recover_prob*self.infectors[-1])
        self.recovers.append(self.recovers[-1] + self.recover_prob*self.infectors[-1])
        
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers, self.exposed
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        plt.plot(self.recovers, label= u"Recovers")
        plt.plot(self.exposed, label= u"Exposed")
        
        plt.legend()
        plt.show()        

# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数        
# infect_prob 传染概率
# recover_prob 康复概率
# e_contactors_num 潜伏者者接触易感者的人数
# e_infect_prob 潜伏者传染概率        
# alpha_prob 潜伏者转化为感染者概率
#导入潜伏期人群（潜伏期具有传染性）
class SEIR_Wuhan(infection_model):
    def __init__(self,
                 population= 10000, 
                 infectors_num= 1, 
                 contactors_num= 10, 
                 infect_prob= 0.05,
                 recover_prob= 0.1,
                 e_contactors_num= 10, 
                 e_infect_prob= 0.03,                 
                 alpha_prob= 0.1):
        
        super(SEIR_Wuhan, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.e_contactors_num = e_contactors_num
        self.e_infect_prob = e_infect_prob
        self.alpha_prob = alpha_prob
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
    
        recovers= []
        recovers.append(0)
        self.recovers = recovers     
        
        exposed= []
        exposed.append(0)
        self.exposed= exposed
            
    def update(self):
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population - self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.exposed.append(self.exposed[-1] + self.contactors_num*self.infect_prob*self.suspectors[-1]*self.infectors[-1]/self.population - self.alpha_prob*self.exposed[-1] + self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.infectors.append(self.infectors[-1] + self.alpha_prob*self.exposed[-1] - self.recover_prob*self.infectors[-1])
        self.recovers.append(self.recovers[-1] + self.recover_prob*self.infectors[-1])
  
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers, self.exposed
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        plt.plot(self.recovers, label= u"Recovers")
        plt.plot(self.exposed, label= u"Exposed")
        
        plt.legend()
        plt.show()        

# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数        
# infect_prob 传染概率
# recover_prob 康复概率
# e_contactors_num 潜伏者者接触易感者的人数
# e_infect_prob 潜伏者传染概率        
# alpha_prob 潜伏者转化为感染者概率
# blockday 隔离介入的时间        
#导入隔离介入（潜伏期具有传染性）
class SEIR_Wuhan_Blocked(infection_model):
    def __init__(self,
                 population= 10000, 
                 infectors_num= 1, 
                 contactors_num= 10, 
                 infect_prob= 0.05,
                 recover_prob= 0.1,
                 e_contactors_num= 10, 
                 e_infect_prob= 0.03,                 
                 alpha_prob= 0.1,
                 blockday= 25):
        
        super(SEIR_Wuhan_Blocked, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.e_contactors_num = e_contactors_num
        self.e_infect_prob = e_infect_prob
        self.alpha_prob = alpha_prob
        self.blockday = blockday
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
    
        recovers= []
        recovers.append(0)
        self.recovers = recovers     
        
        exposed= []
        exposed.append(0)
        self.exposed= exposed
            
    def update(self):
        if self.interval> self.blockday:
            self.contactors_num= 5
            self.e_contactors_num= 5
            
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population - self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.exposed.append(self.exposed[-1] + self.contactors_num*self.infect_prob*self.suspectors[-1]*self.infectors[-1]/self.population - self.alpha_prob*self.exposed[-1] + self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.infectors.append(self.infectors[-1] + self.alpha_prob*self.exposed[-1] - self.recover_prob*self.infectors[-1])
        self.recovers.append(self.recovers[-1] + self.recover_prob*self.infectors[-1])
  
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers, self.exposed
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        plt.plot(self.recovers, label= u"Recovers")
        plt.plot(self.exposed, label= u"Exposed")
        
        plt.legend()
        plt.show()                

# population 人口总数
# infectors_num 感染者人数
# contactors_num 感染者接触易感者的人数        
# infect_prob 传染概率
# recover_prob 康复概率
# e_contactors_num 潜伏者者接触易感者的人数
# e_infect_prob 潜伏者传染概率        
# alpha_prob 潜伏者转化为感染者概率
# blockday 隔离介入的时间       
# death_prob 感染者死亡率        
# p 人口流入率         
#导入人口变化&感染者死亡因素（潜伏期具有传染性）
class SEIR_wuhan_Modified(infection_model):
    def __init__(self,
                 population= 10000, 
                 infectors_num= 1, 
                 contactors_num= 10, 
                 infect_prob= 0.05,
                 recover_prob= 0.1,
                 e_contactors_num= 10, 
                 e_infect_prob= 0.03,                 
                 alpha_prob= 0.1,
                 death_prob= 0.035,
                 p_ratio= 10,
                 blockday= 25):
        
        super(SEIR_wuhan_Modified, self).__init__()
        self.population = population
        self.contactors_num = contactors_num
        self.infect_prob = infect_prob
        self.recover_prob = recover_prob
        self.contactors_num = contactors_num
        self.e_contactors_num = e_contactors_num
        self.e_infect_prob = e_infect_prob
        self.alpha_prob = alpha_prob
        self.death_prob = death_prob
        self.p_ratio = p_ratio
        self.blockday = blockday
        self.interval = 0
        
        infectors= []
        infectors.append(infectors_num)
        self.infectors = infectors
    
        suspectors= [] 
        suspectors.append(population - infectors_num)
        self.suspectors = suspectors
    
        recovers= []
        recovers.append(0)
        self.recovers = recovers     
        
        exposed= []
        exposed.append(0)
        self.exposed= exposed
            
    def update(self):
        if self.interval> self.blockday:
            self.contactors_num= 5
            self.e_contactors_num= 5

        p = 1.0 + random.randint(-1*self.p_ratio, self.p_ratio)/self.population
        self.population = self.population*p
       
        self.suspectors.append(self.suspectors[-1] - self.contactors_num*self.infect_prob*self.infectors[-1]*self.suspectors[-1]/self.population - self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.exposed.append(self.exposed[-1] + self.contactors_num*self.infect_prob*self.suspectors[-1]*self.infectors[-1]/self.population - self.alpha_prob*self.exposed[-1] + self.e_contactors_num*self.e_infect_prob*self.suspectors[-1]*self.exposed[-1]/self.population)
        self.infectors.append(self.infectors[-1] + self.alpha_prob*self.exposed[-1] - self.recover_prob*self.infectors[-1])
        self.recovers.append(self.recovers[-1] + self.recover_prob*self.infectors[-1])
  
        self.interval += 1
        
    def getData(self):
        return self.suspectors, self.infectors, self.recovers, self.exposed
    
    def plotRes(self):
        plt.plot(self.suspectors,  label= u"Susceptibles")
        plt.plot(self.infectors, label= u"Infectors")
        plt.plot(self.recovers, label= u"Recovers")
        plt.plot(self.exposed, label= u"Exposed")
        
        plt.legend()
        plt.show()                
        
if __name__ == '__main__':
   
    '''
    #model= SI()
    #model= SIR()    
    #model= SIS() 
    #model= SEIR()
    #model= SEIR_Wuhan()
    #model= SEIR_Wuhan_Blocked(blockday = 10)
    model= SEIR_wuhan_Modified(blockday = 10)
    
    for i in range(200):
        model.update()
        
    model.plotRes()
    print(model.getMaxInfectors())
    '''
    
    plt.figure(figsize=(12,6))    
    plt.ion()

    value = []
    pos= []
    period= 40
    for i in range(period):
        
        plt.cla()
        model = SEIR_Wuhan_Blocked(blockday= i)
        
        for day in range(200):
            model.update()
        
        model.plotRes()
        plt.pause(0.1)
        
        maxValue, maxPos = model.getMaxInfectors()
        print(i, maxValue, maxPos)
         
    plt.ioff()
    plt.show() 