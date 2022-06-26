# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 03:04:14 2022

@author: asna9
"""

import numpy as np
import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')

# 각 나라별 환자 수와 사망자 수 보기
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
print("<나라별 환자 수와 사망자 수>")
print(ebola_long.head())
print("="*80)

# split()에 '_' 사용해 분리
variable_split = ebola_long.variable.str.split('_') # 문자열 메소드를 사용 x => str을 사용해 문자열로 변환

# 분리된 데이터 전체는 시리즈 type, 특정 위치의 데이터는 리스트 타입
print("<split data>")
print(variable_split.head(), end='\n\n')
print("특정 위치 data:", variable_split[0])

print("="*80)

# data 가져오기
status_value = variable_split.str[0] #시리즈이기 때문에 문자열로 변환
print(status_value.head())

country_values = variable_split.str.get(1) # get() 이용
print(country_values[-5:])
print("="*80)

# dataframe로 split
variable_split = ebola_long.variable.str.split('_', expand=True)
variable_split.columns = ['status', 'country']
print("<dataframe로 split>")
print(variable_split.head())
print("="*80)

# data connect
ebola_parsed = pd.concat([ebola_long, variable_split], axis=1)
print("<data connect>")
print(ebola_parsed.head())
print("="*80)