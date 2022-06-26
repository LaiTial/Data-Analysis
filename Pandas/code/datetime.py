# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:11:06 2022

@author: asna9
"""

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

# dtype 속성을 사용하면 시리즈에 저장된 데이터 타입을 얻어올 수 있다.
print(scientists['Born'].dtype) # object => 파이썬의 문자열(str)은 판다스에서는 object 타입!
print(scientists['Died'].dtype)

# 문자열 날짜 데이터 -> datetime 자료형으로 변환
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

# 변형한 born_datetime, died_datetime를 dataFrame에 추가.
scientists['born_dt'], scientists['died_dt'] = born_datetime, died_datetime

# 얼마동안 세상을 살다 떠났는지 계산
scientists['age_days_dt'] = scientists['died_dt'] - scientists['born_dt']

print("\n[life days]")
print(scientists[['Name','age_days_dt']])