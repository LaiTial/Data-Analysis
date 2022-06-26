# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:10:44 2022

@author: asna9

pandas Series 생성.
아무 데이터나, 문자열을 인덱스로 시리즈도 생성!
"""

import pandas as pd

# 시리즈 생성1
s = pd.Series(['banana', 42])
print(s, end='\n\n')

# 시리즈 생성2
s = pd.Series(['Wes MaKinney', 'Creator of Pandas'])
print(s, end='\n\n')

# 시리즈 생성3 - 문자열을 인덱스로!
s = pd.Series(['Wes MaKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s, end='\n\n')