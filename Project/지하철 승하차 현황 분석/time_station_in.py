# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:50:08 2022

@author: asna9
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from dataS import dataSet

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'gulim'

df_in, df_out = dataSet()

#최근 월을 기준으로 한 데이터프레임 생성
df_in08 = df_in[df_in['사용월']=='202108']
df_out08 = df_out[df_out['사용월']=='202108']

#승차정보 집계 데이터 만들기
df_in08_agg = df_in08.copy()
df_in08_agg.index = df_in08_agg['지하철역'] #지하철역으로 index 변경
df_in08_agg.drop(columns=['사용월', '호선명', '지하철역'], inplace=True) #컬럼삭제

#행과 열 합계
df_in08_agg.loc['sum'] = df_in08_agg.apply('sum', axis=0) #하루 이용집계
df_in08_agg['sum'] = df_in08_agg.apply('sum', axis=1) #지하철역의 이용집계

#시간대별 승차건수
s_in = df_in08_agg.loc['sum'][:-1]

#시간대별 승차건수 시각화
plt.xticks(rotation=90)
plt.bar(s_in.index, s_in.values)
plt.show()

#지하철역별 승차건수
station_in = df_in08_agg['sum'][:-1].sort_values(ascending=False)[:10] #하루종일 승차건수가 많은 역 확인
print(station_in)