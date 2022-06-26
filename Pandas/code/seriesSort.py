# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:37:02 2022

@author: asna9
시리즈 데이터를 sort
"""

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')
ages = scientists['Age']

# sort_index() - 인덱스를 정렬
# ascending=False 옵션을 지정하면 내림차순으로 정럴
print("[인덱스 정렬]")
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)

# sort_values() - 데이터를 정렬
print("\n[데이터 정렬]")
rev_ages = ages.sort_values(ascending=False)
print(rev_ages)

# 벡터와 벡터의 연산은 정렬 여부와 관계 x
rev_ages = ages.sort_index(ascending=False)

print("\n[ages + rev_ages:]")
for age in ages + rev_ages:
    print('{0:4d}'.format(age), end = ' ')
print()

print("\n[ages * 2:]")
for age in ages * 2:
    print('{0:4d}'.format(age), end = ' ')