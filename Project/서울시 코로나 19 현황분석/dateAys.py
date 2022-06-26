# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 01:27:55 2022

@author: asna9

일별 확진자수 분석
확진일, 지역별 확진자수 피봇테이블을 만들어 일별 확진자수를 분석, 시각화시킨다.
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt

#전처리된 데이터를 받는다.
df = dS()

#확진일, 지역별 확진자수 
di_gu = df.pivot_table(index='확진일', columns='지역', values='연번', aggfunc='count', margins=True)

#서울시 일별 확진자수
s_date = di_gu['All'][:-1]

#서울시 일별 확진자가 많았던 순서대로 보기
s_date.sort_values(ascending=False).iloc[:10]

#서울시 일별 확진자 시각화
index, value = s_date.index, s_date.values

plt.plot(index, value)
plt.title("covid-19")
plt.xlabel('Date')
plt.ylabel('Num')
plt.xticks(rotation=45)
plt.show()
