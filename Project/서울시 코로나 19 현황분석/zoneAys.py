# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:49:48 2022

@author: asna9

지역별 확진자수 분석
총 확진자수를 구별로 분석, 최근일 확진자수도 분석
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt
import matplotlib as mpl

def drawG(data, title):
    
    index, value = data.index, data.values
    
    mpl.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.family'] = 'gulim'

    plt.figure(figsize=(11,6))
    plt.title(title, size=20)
    plt.xlabel('Zone')
    plt.ylabel('Num')
    
    plt.barh(index, value)
    plt.show()

#전처리된 데이터를 받는다.
df = dS()

#확진일, 지역별 확진자수 
di_gu = df.pivot_table(index='확진일', columns='지역', values='연번', aggfunc='count', margins=True)

#서울시 구별 확진자수
s_gu = di_gu.loc['All'][:-1]

#서울시 구별 확진자가 많았던 순서대로 보기
s_gu = s_gu.sort_values(ascending=False)

#서울시 구별 확진자 시각화
drawG(s_gu, 'All covid-19')

#최근일 기준 지역별 확진자 수 
s_gu = di_gu.iloc[-2][:-1]
s_gu = s_gu.sort_values(ascending=False)

#최근일 기준 지역별 확진자 수 시각화
drawG(s_gu, 'Now covid-19')