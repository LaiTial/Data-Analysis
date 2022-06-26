# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:41:39 2022

@author: asna9

배열을 추가하는 메소드.
append(), insert(), delete()
"""

import numpy as np

a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(10, 19, (3, 3))

print("array a:", a, end='\n\n')
print("array b:", b, end='\n\n')

# append()
# axis를 지정하지 않았을 경우
result = np.append(a, b)
print("Append - axis=None:", result, end='\n\n')

# axis=0으로 지정한 경우
result = np.append(a, b, axis=0) # a배열의 아래쪽에 b배열이 추가
print("Append -axis=0:", result, end='\n\n')

# axis=1으로 지정한 경우
result = np.append(a, b, axis=1) # a배열의 오른쪽에 b배열이 추가된다.
print("Append -axis=1:", result, end='\n\n')

# insert()
print("Insert - axis=None:", np.insert(a, (1,5), 99999), end='\n\n') # axis 지정 x, 1차원 배열로 변경
print("Insert - axis=0:", np.insert(a, 1, 99999, axis=0), end='\n\n') # axis = 0, 행[1]
print("Insert - axis=1:", np.insert(a, 1, 99999, axis=1), end='\n\n') # axis = 1, 열[1]

# delete()
print("Delete - axis=None:", np.delete(a, 1), end='\n\n') # axis 지정 x, 1차원 배열로 변경
print("Delete - axis=0:", np.delete(a, 1, axis=0), end='\n\n') # axis = 0, 행[1]
print("Delete - axis=1:", np.delete(a, 1, axis=1), end='\n\n') # axis = 1, 열[1]

