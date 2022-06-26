# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:21:15 2022

@author: asna9

행 단위 데이터 추출하기.
loc[]와 iloc[]로 데이터 추출 test.
"""
import numpy as np
import pandas as pd

gapM = pd.read_csv("../data/gapminder.tsv", sep='\t')

#loc로 첫번째 data print
print(gapM.loc[0])
print('=' * 80)

#loc로 마지막 data print
print(gapM.loc[1703])
print('=' * 80)

# 마지막 데이터 추출하기 => shape[0] 이용
print(gapM.loc[gapM.shape[0] - 1])
print('=' * 80)

# 마지막 데이터 추출하기 => tail() 메소드를 이용
print(gapM.tail(1))
print('=' * 80)

# 여러 인덱스의 데이터를 한꺼번에 추출
print(gapM.loc[[0, 99, 999]])

# iloc로 마지막 data
print(gapM.iloc[1703])
print('=' * 80)

print(gapM.iloc[-1])
print('=' * 80)

# iloc[]로 여러 인덱스의 데이터를 한꺼번에 추출
print(gapM.iloc[[0, 6, 399]])