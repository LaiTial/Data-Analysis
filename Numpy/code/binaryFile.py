# -*- coding: utf-8 -*-
"""
배열 객체를 이진 파일에 저장&불러오기
@author: asna9
"""

import numpy as np

np.random.seed(100)
a = np.random.randint(0, 10, (2, 3))
print("배열 a: ", end='')
print(a, end='\n\n')

b = np.random.randint(0, 10, (3, 3))
print("배열 b: ", end='')
print(b, end='\n\n')

# 배열 객체 저장 - 바이너리 파일

# a 배열을 파일로 저장
np.save('../output/my_array1', a)

# a, b 배열을 파일로 저장
np.savez('../output/my_array2', a, b)

# np.load() 메소드로 npy, npz 파일에서 데이터를 읽는다.

# npy 파일 읽기
print("npy 파일을 읽은 결과: ", end='')
print(np.load('../output/my_array1.npy'), end='\n\n')

# npz 파일 읽기
print("npz 파일을 읽은 결과: ", end='')
print(np.load('../output/my_array2.npz'), end='\n\n') # <numpy.lib.npyio.NpzFile object at 0x000001DA4FC7AA58>

npzFile = np.load('../output/my_array2.npz')

print("npzFile['arr_0']: ", end='')
print(npzFile['arr_0'], end='\n\n')

print("npzFile['arr_1']: ", end='')
print(npzFile['arr_1'])