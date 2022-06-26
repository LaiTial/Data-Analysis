# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:07:56 2022

@author: asna9

seaborn 라이브러리의 샘플 데이터를 불러온다.
그리고 자료형을 변환하고 확인
"""

import numpy as np
import pandas as pd
import seaborn as sns

#'tips'는 searborn에서 제공하는 샘플데이터다!
tips = sns.load_dataset('tips')

# 데이터 print
print("<Data>")
print(tips)
print("="*80)

# astype() - 자료형 변환
# time : category -> 문자열
tips['time_str'] = tips['time'].astype(str)
print("<자료형 변환 확인>")
print(tips.dtypes)