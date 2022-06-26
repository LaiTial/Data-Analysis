# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:36:32 2022

@author: asna9

에볼라 바이러스 발병 데이터
Cases_* => 발병 국가, Deaths_* => 사망자 수

데이터를 읽어서 누락값을 count
"""

import numpy as np
import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')

# count_nonzero() : 배열에서 0(False)이 아닌 데이터의 개수를 count
print("0이 아닌 data의 개수:",np.count_nonzero([False, 0, True, 1, 999, np.NaN]))

# 읽은 data의 누락값
print("all NaN:",np.count_nonzero(ebola.isnull())) # 누락값의 개수를 센다.
print("Cases_Guinea NaN:",np.count_nonzero(ebola['Cases_Guinea'].isnull()))

# count() : 누락값이 아닌 데이터의 count
print("\n[No NaN]")
print(ebola.count())
print("="*80)

# shape 사용
# 전체 데이터의 개수 - 누락값이 아닌 데이터의 개수
num_row = ebola.shape[0]
num_missing = num_row - ebola.count()
print("[All NaN]")
print(num_missing)
print("="*80)

# value_counts() : 지정한 열의 빈도수 get
# '.' 사용
print("[빈도수 count]")
print(ebola.Cases_Guinea.value_counts())
print("="*80)

# NaN도 count
print("[NaN 포함 빈도수 count]")
print(ebola.Cases_Guinea.value_counts(dropna=False))
print("="*80)

# 기초 통계를 계산하는 메소드 - 누락값을 무시
print("sum():",ebola.Cases_Guinea.sum())
print("sum(skipna=True):",ebola.Cases_Guinea.sum(skipna=True))
print("sum(skipna=False):",ebola.Cases_Guinea.sum(skipna=False))
print("mean():",ebola.Cases_Guinea.mean())
print("max():",ebola.Cases_Guinea.max())
print("min():",ebola.Cases_Guinea.min())
print("count():",ebola.Cases_Guinea.count())