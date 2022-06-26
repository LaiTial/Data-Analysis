# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:04:45 2022

@author: asna9
"""

import random as r
import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

# shuffle() - 데이터 scramble
age = scientists['Age'].copy()
r.shuffle(age) # scientists 데이터프레임의 Age 열만 섞인다.

scientists['Age'] = age
print(scientists)
print("="*80)

# drop() - 열 삭제
scientists_dropped = scientists.drop(['Age', 'Occupation'], axis=1)
print(scientists_dropped)
print("="*80)

# to_pickle() : 데이터를 피클로 저장
names = scientists['Name']
names.to_pickle('../output/scientists_name_series.pickle')

# read_pickle() : 피클을 읽어온다
scientists_names_from_pickle = pd.read_pickle('../output/scientists_name_series.pickle')
print(scientists_names_from_pickle)
print("="*80)

# 데이터프레임도 피클로 저장 가능
scientists.to_pickle('../output/scientists_df.pickle')
scientists_from_pickle = pd.read_pickle('../output/scientists_df.pickle')
print(scientists_from_pickle)

# to_csv() : csv 파일로 저장
names.to_csv('../output/scientists_name_series.csv')
scientists.to_csv('../output/scientists_df.tsv', sep='\t')