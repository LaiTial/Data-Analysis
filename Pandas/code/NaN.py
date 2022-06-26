# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:21:10 2022

@author: asna9

누락값 확인하는 여러 방법
누락값과 다른 값 비교
"""

# 누락값 라이브러리 import
from numpy import NaN, NAN, nan
import pandas as pd

# 누락값과 비교
print("NaN == True:",NaN == True)
print("NaN == False:",NaN == False)
print("NaN == 0:",NaN == 0)
print("NaN == '':",NaN == '')

# 누락값과 자기 자신과 비교
print("\nNaN == NaN:",NaN == NaN)
print("NaN == NAN:",NaN == NAN)
print("NaN == nan:",NaN == nan)

# 판다스에서는 누락값을 확인하는 isnull(), isna() 메소드가 있고 누락값이면 True, 누락값이 아니면 False를 리턴한다.
print("\nisnull(NaN):",pd.isnull(NaN))
print("isnull(0):",pd.isnull(0))
print("isnull(''):",pd.isnull(''))
print("isna(NaN):",pd.isna(NaN))
print("isna(0):",pd.isna(0))
print("isna(''):",pd.isna(''))

# 반대의 경우(누락값이 아닌 경우)도 검사하는 notnull(), notna() 메소드가 있고 누락값이 아니면 True, 누락값이면 False를 
# 리턴한다.
print("\nnotnull(NaN):",pd.notnull(NaN))
print("notnull(0):",pd.notnull(0))
print("notnull(''):",pd.notnull(''))
print("notna(NaN):",pd.notna(NaN))
print("notna(0):",pd.notna(0))
print("notna(''):",pd.notna(''))