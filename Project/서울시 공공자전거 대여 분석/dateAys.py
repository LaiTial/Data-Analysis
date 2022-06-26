# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:31:39 2022

@author: asna9
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt

#전처리된 데이터를 받는다.
df = dS()

#대여날짜 컬럼 추가
df['대여날짜'] = df['대여일시'].dt.date

#대여날짜별 대여건수
df_count = df.groupby('대여날짜').대여일시.count().to_frame()
df_count.columns=['대여건수']

#대여날짜별 대여건수 시각화
plt.title("date Use")
plt.plot(df_count.index, df_count.values)
plt.show()

#대여날짜별 이용시간
df_time = df.groupby('대여날짜')['이용시간'].sum().to_frame()

#대여날짜별 이용시간 시각화
plt.title("date UseTime")
plt.plot(df_time.index, df_time.values)
plt.show()

#대여날짜별 이용거리
df_distance = df.groupby('대여날짜')['이용거리'].sum().to_frame()

#대여날짜별 이용거리 시각화
plt.title("date UseDistance")
plt.plot(df_distance.index, df_distance.values)
plt.show()

#대여날짜별 현황을 보기 위해 하나의 dataframe으로 합치기
df_date = pd.concat([df_count, df_time, df_distance], axis=1)