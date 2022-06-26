# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:48:53 2022

@author: asna9

concat으로 dataframe 연결,
시리즈와 데이터프레임 연결, 
열과 행 단위의 데이터프레임 생성
"""

import numpy as np
import pandas as pd

#데이터 읽기
df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

# concat() : dataframe 연결
row_concat = pd.concat([df1, df2, df3])
print("dataframe끼리 연결")
print(row_concat)
print("="*80)

# 데이터프레임에 시리즈 연결 - 기본
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4']) # 리스트를 시리즈로 변환
tempConcat = pd.concat([df1, new_row_series])
print("series와 dataframe 연결 - 기본")
print(tempConcat)
print("="*80)

# series -> dataframe
print("열 단위의 데이터프레임 생성")
array = pd.DataFrame(['n1', 'n2', 'n3', 'n4']) # 열 단위의 데이터프레임이 생성
print(array)
print("="*80)

print("행 단위의 데이터프레임 생성")
array = pd.DataFrame([['n1', 'n2', 'n3', 'n4']]) # 행 단위의 데이터프레임이 생성
print(array)
print("="*80)

# 열 이름 지정
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])
print("열 이름 지정")
print(new_row_df)
print("="*80)

# 데이터프레임에 시리즈 연결 - 변형
row = pd.concat([df1, new_row_df])
print("series와 dataframe 연결 - 변형")
print(row)
