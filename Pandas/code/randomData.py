# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:07:30 2022

@author: asna9

누락값을 평균값으로 처리
랜덤으로 데이터 4개를 추출해 NaN 값으로 변경
"""

import numpy as np
import pandas as pd
import seaborn as sns

# 성별을 구분해서 total_bill 열의 데이터를 받아 평균을 계산하는 함수
# 누락값을 평균으로 채우는 역할.
def fill_na_mean(x):
    avg = x.mean()
    return x.fillna(avg)

# total_bill의 값 4개를 임의로 누락값으로 변경
# sample() : 전체 데이터에서 랜덤하게 데이터를 추출
np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
print("[random으로 data 추출]")
print(tips_10)
print("="*80)

# shuffle(), permutation() : 무작위로 배열을 scramble
# shuffle - 원본 수정, permutation - 복사본

x = np.arange(10)
print("원본:",x) # 원본
print("permutation(x):",np.random.permutation(x)) # scramble

print("\n원본:",x) # 원본 => 원본을 변형 x
print("shuffle(x):",np.random.shuffle(x)) # None => 섞어서 리턴된 값이 없다. => 원본을 섞어 버렸다.
print("\n원본:",x) # 원본이 섞여 출력

# random으로 선택한 4개 NaN으로 변경
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN
print("="*80)
print("[random으로 선택한 4개 NaN으로 변경]")
print(tips_10)
print("="*80)

# 누락값을 단순히 전체 평균으로 채우면 x
# 여성 < 남성이니 구분해서 평균값을 구하지 않으면 여성 data가 남성 data의 영향(간섭)을 받아서 훼손될 수 있다.
# 성별별로 그룹화 - 남성의 누락값은 3개, 여성의 누락값은 1개
count_sex = tips_10.groupby('sex').count() #누락값 count

total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
print("[각 그룹 평균으로 NaN값 채우기]")
print(total_bill_group_mean)


