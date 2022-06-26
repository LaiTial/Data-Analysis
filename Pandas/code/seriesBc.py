# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:45:14 2022

@author: asna9

브로드캐스팅 연산
"""

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

ages = scientists['Age']

print("Age :", end='')
for age in ages:
    print('{0:4d}'.format(age), end = ' ')
print()

# 같은 길이의 벡터로 연산
print("V+V :", end='')
for age in ages + ages:
    print('{0:4d}'.format(age), end = ' ')
print()

print("V*V :", end='')
for age in ages * ages:
    print('{0:5d}'.format(age), end = ' ')
print()

# 벡터에 스칼라 값을 연산
print("V+100 :", end='')
for age in ages + 100:
    print('{0:4d}'.format(age), end = ' ')
print()

print("V*2 :", end='')
for age in ages * 2:
    print('{0:4d}'.format(age), end = ' ')
print("\n")

# 길이가 서로 다른 벡터를 연산
print(ages + pd.Series([1, 100]))