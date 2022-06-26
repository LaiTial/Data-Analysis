# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:04:29 2022

@author: asna9
"""
import numpy as np
import pandas as pd

#데이터 읽기
df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

col_concat = pd.concat([df1, df2, df3], axis=1)

# 열 이름으로 데이터 추출
print("열 이름으로 데이터 추출")
print(col_concat['A'])
print("="*80)

# 새로운 열을 추가
col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print("새로운 열을 추가")
print(col_concat)
print("="*80)

# 열 이름을 변경
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

row_concat = pd.concat([df1, df2, df3], ignore_index=True)
print("서로 다른 열 이름을 가진 dataframe 연결")
print(row_concat)
print("="*80)

# 공통 열만 연결 df1-df3
print("공통 열만 연결 df1-df3")
con = pd.concat([df1, df3], join='inner')
print(con)
print("="*80)

# 인덱스 변경
df3.index = [0, 2, 5, 6]
df3.index = [0, 2, 5, 6]

# axis=1로 dataframe 연결
col_concat = pd.concat([df1, df2, df3], axis=1)
print("서로 다른 열 이름을 가진 dataframe 연결 axis-1")
print(col_concat)
print("="*80)
