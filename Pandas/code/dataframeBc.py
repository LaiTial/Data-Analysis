# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:51:04 2022

@author: asna9

데이터프레임의 boolIndexing, broadcasting
"""

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

#원본 데이터
print(scientists)
print('=' * 80)

# bool index & broadcasting
print(scientists[scientists['Age'] > scientists['Age'].mean()])

# 시리즈에 스칼라 연산
print('=' * 80)
print(scientists * 2)