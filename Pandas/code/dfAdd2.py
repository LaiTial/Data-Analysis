# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:51:04 2022

@author: asna9

append로 데이터프레임 연결,
인덱스 재지정,
딕셔너리를 dataframe에 추가
"""

import numpy as np
import pandas as pd

#데이터 읽기
df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])

# append로 데이터 추가
row = df1.append(new_row_df)
print("append로 data 추가")
print(row)
print("="*80)

# 인덱스 지정 - append
row = df1.append(new_row_df, ignore_index=True)
print("인덱스 재부여 - append")
print(row)
print("="*80)

# 딕셔너리를 dataframe에 추가
data_dict = {'A': 'n5', 'B': 'n6', 'C': 'n7', 'D': 'n8'}
row = df1.append(data_dict, ignore_index=True)
print("딕셔너리를 dataframe에 추가")
print(row)
print("="*80)

# 인덱스 재부여 - concat
row_concat = pd.concat([df1, df2, df3], ignore_index=True)
print("인덱스 재부여 - concat")
print(row_concat)
print("="*80)

# concat - 오른쪽으로
col_concat = pd.concat([df1, df2, df3], axis=1)
print("concat - 오른쪽으로")
print(row_concat)
print("="*80)

# concat - 오른쪽으로, 인덱스 재지정
col_concat = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
print("concat - 오른쪽으로")
print(row_concat)
print("="*80)