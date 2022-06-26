# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:16:03 2022

@author: asna9

groupby, agg메소드로 사용자정의 함수 test
"""

import numpy as np
import pandas as pd
import seaborn as sns
import groupbyMethod as gm

df = pd.read_csv('../data/gapminder.tsv', sep='\t')

# groupby() : 데이터 그룹화
age_lifeExp_by_year = df.groupby('year').lifeExp.mean()

# agg로 data에 일괄 적용
agg_my_mean = df.groupby('year').lifeExp.agg(gm.my_mean)
print("[agg로 data에 일괄 적용]")
print(agg_my_mean)
print("="*80)

# 전체 평균을 계산
global_mean = df.lifeExp.mean()

# agg() 호출
agg_mean_diff = df.groupby('year').lifeExp.agg(gm.my_mean_diff, global_mean) # diff_value = global_mean 해도 됨
print("[그룹 평균과 전체 평균의 편차 계산]")
print(agg_mean_diff)
print("="*80)

# 1개 열에 여러 함수 실행
gdf = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
print("[1개 열에 여러 함수 실행]")
print(gdf)
print("="*80)

# 여러개의 열에 대해서 여러개의 함수를 실행
gdf = df.groupby('year').agg({'lifeExp': 'mean', 'pop': 'median', 'gdpPercap': 'median'})
print("[여러개의 열에 대해서 여러개의 함수를 실행]")
print(gdf)
print("="*80)

# transform() : 그룹별 계산을 통해 데이터프레임 자체를 변환
df['zscore'] = df.groupby('year').lifeExp.transform(gm.my_zscore)
print("[transform()]")
print(df)
print("="*80)
