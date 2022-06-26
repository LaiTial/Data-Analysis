# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:25:47 2022

@author: asna9

열 단위 데이터 추출하기
속성 이름(열 이름) 사용해 데이터 추출.
"""

import pandas as pd

gapM = pd.read_csv("../data/gapminder.tsv", sep='\t')

country = gapM['country'] # 데이터프레임에서 1개의 열만 얻어오려면 열 이름만 사용하면 된다.

print("data HEAD:",gapM.head(2), end='\n\n')
print("data TAIL:",gapM.tail(2), end='\n\n')

# 2개 이상의 열을 추출
sub_set = gapM[['country', 'continent', 'year']]
print("data Many:\n", sub_set.head(5))