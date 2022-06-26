# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:15:25 2022

@author: asna9

gapminder - 국가별 경제 수준과 의료 수준 동향을 정리한 DataSet

lifeExp : 기대수명,
pop : 인구 수,
gdpPercap : 1인당 
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

gapM = pd.read_csv("./gapminder.tsv", sep='\t')

# continent열로 그룹화
continent = gapM.groupby('continent')

# 대륙별로 year로 그룹화 -> lifeExp 열만 추출
for key, group in continent:
    
    yearly = group.groupby('year')
    
    printData = ['lifeExp', 'pop', 'gdpPercap']
    dataT = ['chartreuse', 'turquoise', 'mediumslateblue']
    lineS = ['-.', 'solid', 'dotted']
    
    i=0
    
    for data in printData:
        
        plt.cla()
        
        dataS = yearly[data].mean()
        
        plt.plot(dataS, label=data, color=dataT[i], linestyle=lineS[i])
        plt.title(key)    
        plt.legend(loc=1)
        plt.show()

        time.sleep(2)
        
        i += 1

