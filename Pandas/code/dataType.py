# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:40:00 2022

@author: asna9

pandas가 가지고 있는 method(), 속성 test
"""

import numpy as np
import pandas as pd

gapM = pd.read_csv("../data/gapminder.tsv", sep='\t')

# pandas가 가지고 있는 메소드
print("data HEAD:",gapM.head(), end='\n\n')
print("data TAIL:",gapM.tail(1), end='\n\n')

# 속성과 dtypes
print("data Shapes:", gapM.shape, end='\n\n')
print("data Columns:", gapM.columns, end='\n\n')
print("data Dtypes:", gapM.dtypes, end='\n\n')

# 데이터의 정보를 가져오는 info()
print("data Info:", gapM.info())