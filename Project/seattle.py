# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:35:11 2022

@author: asna9

2014년 시애틀 강수량 데이터 <= Seattle2014.csv
이 데이터를 읽어 각 달의 평균 강수량을 구한다.

강수량 데이터는 'PRCP'열에 존재!
"""

import pandas as pd
import numpy as np

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
rain_jan = []

# 판다스의 read_csv() 메소드로 csv 파일을 읽는다.
rain_in_seattle = pd.read_csv('./Seattle2014.csv')

# 강수량 데이터만 추출
rain_arr = rain_in_seattle['PRCP'].values
days_arr = np.arange(0, 365) # 날짜 배열 생성

# 누적 날짜 배열 생성
dates = np.array(dates)
dates = dates.cumsum()

for i in range(12):
    
    start=0
    
    if(i > 0):
        start = dates[i-1]
    
    end = dates[i]
    
    condition_jan = (days_arr < end) & (days_arr >= start) # 브로드캐스팅으로 달별로 불린 배열 생성

    # 각 달의 강수량만 뽑아낸다.

    rain_jan.append(rain_arr[condition_jan])
    

for i in range(12):
    print('{}월 강수량 합계 : {}'.format(i+1, np.sum(rain_jan[i])))
    print('{}월 강수량 평균 : {}\n'.format(i+1, np.mean(rain_jan[i])))