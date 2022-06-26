# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:24:15 2022

@author: asna9
numpy 라이브러리에서 사용하는 함수들 연습
"""

import numpy as np

arr = np.arange(0, 32)

print(arr)

print(len(arr))
print(type(arr))

print(arr.shape) #shape : numpy배열의 차원(demension)을 튜플 형태로 얻어온다.
print(arr.ndim) #ndim : numpy배열의 차원(demension)을 정수로 얻어온다.

# reshape() 함수는 numpy배열의 차원을 변경한다.
v = arr.reshape(4, 2, 4)
print("\n<reshape>한 결과")
print("shape: {0}, ndim: {1}".format(v.shape, v.ndim))