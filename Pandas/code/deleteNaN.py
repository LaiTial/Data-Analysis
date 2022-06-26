# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 02:24:05 2022

@author: asna9

누락값 삭제하기
"""

import numpy as np
import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')

# 데이터 일부분 print
print("[데이터 일부분 print]")
print(ebola.iloc[:10, :5])
print("="*80)

# dropna() : 누락값이 포함된 행을 삭제.
ebola_dropna = ebola.dropna()
print("[누락값이 포함된 행을 삭제 후 data]")
print(ebola_dropna)
print("="*80)

# 파생변수 생성
ebola['Cases_Multi'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']

# 지정한 데이터 가져오기
ebola_sebset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'Cases_Multi']]
print("[지정한 열들의 data]")
print(ebola_sebset)
