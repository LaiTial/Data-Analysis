# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:07:27 2022

@author: asna9

팬시 인덱싱
"""

import numpy as np

a = np.arange(24).reshape(4, 6)

print("array a:", a, end='\n\n')
print("fancy result:",a[:, [1, 2]], end='\n\n')

print("fancy result:",a[1:, [1, 2]], end='\n\n')
print("fancy result:",a[[1,2], [3]], end='\n\n')

a_1 = a[0, 0], a[1, 1], a[2, 2], a[3, 3] # 튜플
a_2 = [a[0, 0], a[1, 1], a[2, 2], a[3, 3]] # 리스트
print("a_1:",a_1)
print("a_2:",a_2)

