# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:05:03 2022

@author: asna9
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt

#전처리된 데이터를 받는다.
df = dS()

#대여시간, 반납시간 컬럼 추가
df['대여시간'] = df['대여일시'].dt.hour
df['반납시간'] = df['반납일시'].dt.hour

#시간대별 대여현황
s_rental = df['대여시간'].value_counts()

#시간대별 반납현황
s_return = df['반납시간'].value_counts()

#시간대별 공공자전거 대여건수 시각화
s_rental = s_rental.sort_index()
plt.title("time-Rental num")
plt.bar(s_rental.index, s_rental.values, color='skyblue')
plt.show()

#시간대별 공공자전거 반납건수 시각화
s_return = s_return.sort_index()
plt.title("time-Return num")
plt.bar(s_return.index, s_return.values, color='pink')
plt.show()
