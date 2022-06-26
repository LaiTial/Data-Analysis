# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:24:35 2022

@author: asna9

자료형 변환
"""

import numpy as np
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

# tips data의 일부분만 뽑아내기
tips_sub_miss = tips.head(10)

# 지정된 행의 'total_bill'값 'missing'으로 변경
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'
print("[지정된 행의 'total_bill'값 'missing'으로 변경]")
print(tips_sub_miss)
print("="*80)

# total_bill -> 실수로 변환 -> 오류
#tips_sub_miss['total_bill'] = tips_sub_miss['total_bill'].astype(float)

# to_numeric() : 문자열을 실수로 변환
#tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'])

# 'raise' - 숫자로 변환할 수 없는 값이 있으면 오류를 발생
#tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='raise')

# 'ignore' - 오류가 발생되면 무시
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='ignore')
print("['ignore' - 오류가 발생되면 무시]")
print(tips_sub_miss)
print("="*80)

# 'coerce' - 오류가 발생된 데이터를 누락값으로 변경
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='coerce')
print("['coerce' - 오류가 발생된 데이터를 누락값으로 변경]")
print(tips_sub_miss)
print("="*80)