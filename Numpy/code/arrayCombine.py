# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:49:21 2022

@author: asna9
배열 결합.
concatenate() 메소드로 축으로 배열을 결합하는 방법과,
정해져있는 vstack()과 hstack()을 test
"""

import numpy as np

a = np.random.randint(1, 10, (2, 3))
b = np.random.randint(1, 10, (2, 3))

print("array a:", a, end='\n\n')
print("array b:", b, end='\n\n')

# concatenate()
# axis=None
result = np.concatenate((a, b)) # axis 생략시 기본값이 0
print("concatenate()-axis=None:", result, end='\n\n')

# axis=0 - 수직 방향으로 결합
result = np.concatenate((a, b), axis=0) # axis=0 방향으로 배열을 결합한다. np.concatenate((a, b))와 결과가 동일하다.
print("concatenate()-axis=0:", result, end='\n\n')

# axis=1 - 수평 방향으로 결합
result = np.concatenate((a, b), axis=1) # axis=1 방향으로 배열을 결합한다.
print("concatenate()-axis=1:", result, end='\n\n')

# vstack() - 수직 방향으로 결합
print("vstack():", np.vstack((a, b)), end='\n\n')

# hstack() - 수평 방향으로 결합
print("hstack():", np.hstack((a, b)), end='\n\n')