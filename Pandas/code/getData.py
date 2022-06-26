# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 18:11:22 2022

@author: asna9

loc, iloc을 사용해 데이터를 추출
"""

import numpy as np
import pandas as pd

gapM = pd.read_csv("../data/gapminder.tsv", sep='\t')

# 슬라이싱
# 모든 행(':')의 데이터에 대해 country, year, pop 열을 추출
subset = gapM.loc[:, ['country', 'year', 'pop']]
print(subset.head(), end='\n\n')

# 모든 행에 대해서 2, 4, -1열(year, pop, 1인당 gdp)을 추출
subset = gapM.iloc[:, [2, 4, -1]]
print(subset.head(), end='\n\n')

# 0~4열(1인당 gdp를 제외한 모든 열)을 추출
subset = gapM.iloc[:, range(5)]
print(subset.head(), end='\n\n')

# 0, 2, 4열(country, year, pop)을 추출
subset = gapM.iloc[:, range(0, 6, 2)]
print(subset.head(), end='\n\n')
