# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:04:25 2022
집계 메소드 - median(), 
@author: asna9
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)

#평균 구하기
print("Mean() 함수 결과")
print("a.mean():", a.mean())
print("a.mean(axis=0):", a.mean(axis=0))
print("a.mean(axis=1):", a.mean(axis=1))

#중위수 구하기
print("Median() 함수 결과")
print("np.median():", np.median(a))
print("np.median(a, axis=0):", np.median(a, axis=0))
print("np.median(a, axis=0):", np.median(a, axis=1), end='\n\n')

#상관계수 구하기
print("Corrcoef() 함수 결과")
print("np.corrcoef(a):", np.corrcoef(a), end='\n\n')

#표준편차 구하기
print("Std() 함수 결과")
print("np.std(a):", np.std(a))
print("np.std(a, axis=0):", np.std(a, axis=0))
print("np.std(a, axis=1):", np.std(a, axis=1))
