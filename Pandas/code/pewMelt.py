# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 02:42:15 2022

@author: asna9

'미국의 소득과 종교' 데이터를 사용
데이터 정리 - 피벗
"""

import numpy as np
import pandas as pd

pew = pd.read_csv('../data/pew.csv')
print("<Data head>")
print(pew.head())
print("="*80)

# all data 피벗
per_long = pd.melt(pew, id_vars='religion')
print("<all data pivot>")
print(per_long.head())
print("="*80)

# 지정된 열만 대상으로 피벗
per_long = pd.melt(pew, id_vars='religion', value_vars='$10-20k')
print("<지정된 data pivot>")
print(per_long.head())
print("="*80)

# 2개 이상의 열 피벗
per_long = pd.melt(pew, id_vars='religion', value_vars=['$10-20k', '$100-150k'])
print("<2개 이상의 열 data pivot>")
print(per_long.head())
print(per_long.tail())
print("="*80)

# 속성 이용
per_long = pd.melt(pew, id_vars='religion', value_vars='$10-20k', var_name='최저임금', value_name='인원수')
print("<Use 속성>")
print(per_long.head())
print("="*80)