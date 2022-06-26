# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:45:52 2022
집계 메소드 - sum(), max(), min(), cumsum(), mean()
@author: asna9
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)

# sum()
#axis=None : 전체 행렬을 하나의 배열로 간주
print("Sum() 함수 결과")
print("[axis=None]")
print("a.sum():", a.sum())
print("a.sum(axis=None):", a.sum(axis=None))
print("np.sum(a):", np.sum(a))
print("np.sum(a, axis=None):", np.sum(a, axis=None), end='\n\n')

# axis=0
print("[axis=0]")
print("a.sum(axis=0):", a.sum(axis=0))
print("np.sum(a, axis=0):", np.sum(a, axis=0), end='\n\n')

# axis=1
print("[axis=1]")
print("a.sum(axis=1):", a.sum(axis=1))
print("np.sum(a, axis=1):", np.sum(a, axis=1), end='\n\n')

# max(), min()
print("Max() 함수 결과")
print("a.max():", a.max())
print("a.max(axis=0):", a.max(axis=0))
print("a.max(axis=1):", a.max(axis=1), end='\n\n')

print("Min() 함수 결과")
print("a.min():", a.min())
print("a.min(axis=0):", a.min(axis=0))
print("a.min(axis=1):", a.min(axis=1), end='\n\n')

#누적합계 결과
print("Cumsum() 함수 결과")
print("a.cumsum():", a.cumsum())
print("a.cumsum(axis=0):", a.cumsum(axis=0))
print("a.cumsum(axis=1):", a.cumsum(axis=1), end='\n\n')






