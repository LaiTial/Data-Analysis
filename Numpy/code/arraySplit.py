# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:22:10 2022

@author: asna9

배열 분할.
배열을 수평 방향으로 분할하는 hsplit() 메소드와 수직 방향으로 분할하는 vsplit() 메소드를 test.
"""

import numpy as np

a = np.arange(1, 25).reshape(4, 6)
print("array a:", a, end='\n\n')

# hsplit() - 수평 방향으로 분할
result = np.hsplit(a, 2)
print("hsplit 2 result:", result, end='\n\n')

result = np.hsplit(a, 3)
print("hsplit 3 result:", result, end='\n\n')

# [1, 3, 5] <= :1, 1:3, 3:5, 5: 이렇게 4개의 그룹으로 분할!
result = np.hsplit(a, [1, 3, 5])
print("hsplit [1, 3, 5] result:", result, end='\n\n')

# vsplit() - 수직 방향으로 분할
result = np.vsplit(a, 2)
print("vsplit 2 result:", result, end='\n\n')

result = np.vsplit(a, 4)
print("vsplit 4 result:", result, end='\n\n')

# [1, 3, 5] <= :1, 1:3, 3:5, 5: 이렇게 4개의 그룹으로 분할!
result = np.vsplit(a, [1, 3, 5])
print("vsplit [1, 3, 5] result:", result, end='\n\n')