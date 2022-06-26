# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:02:21 2022

@author: asna9

배열 변환
행렬 전치시키기, ravel, reshape 행렬 변환.
resize()로 행렬 변환시키기.
"""

import numpy as np

a = np.random.randint(1, 10, (2, 6))

print("array a:", a, end='\n\n')
print("array a.T:", a.T, end='\n\n') # 행렬 전치

# 배열 형태 변경
print("array ravel():",a.ravel(), end='\n\n')
print("array reshape():",a.reshape(3, 2, 2), end='\n\n')

# resize()
b = np.resize(a, (3, 4))
print("array resize() - np:",b, end='\n\n')

a.resize(6, 2)
print("array resize() - a:",a, end='\n\n')

# 요소의 개수가 변경되는 resize
a = np.random.randint(1, 10, (2, 6))

a.resize(2, 10)
print("resize - 0 full:", a, end='\n\n')

a.resize(2, 4)
print("resize - lost:", a)

