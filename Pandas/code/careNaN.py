# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 02:11:15 2022

@author: asna9

데이터에 누락값이 나올 시 대처 방법
"""

import numpy as np
import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')

# 데이터 일부분 print
print("[데이터 일부분 print]")
print(ebola.iloc[:10, :5])
print("="*80)

# fillna() - 누락값을 지정된 값으로 변경
print("[NaN을 지정된 값으로 변경]")
print(ebola.fillna(0).iloc[:10, :5])
print("="*80)

# fillna()+method='ffill' - 누락값이 나타나기 전의 값으로 변경
print("[NaN를 앞의 값으로 변경]")
print(ebola.fillna(method='ffill').iloc[:10, :5])
print("="*80)

# fillna()+method='bfill' -누락값이 나타난 다음 값으로 
print("[NaN를 뒤의 값으로 변경]")
print(ebola.fillna(method='bfill').iloc[:10, :5])
print("="*80)

# interpolate() - 중간값(평균값)으로 누락값을 변경
print("[NaN를 중간값으로 변경]")
print(ebola.interpolate().iloc[:10, :5])
print("="*80)
