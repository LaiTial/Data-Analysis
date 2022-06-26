# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:21:07 2022

@author: asna9

copy한 배열 결과랑 원본 배열 test.
copy한 배열을 바꿨을 시 원본 배열에 영향이 안간다. 이를 코드로 실험.
"""

import numpy as np

a = np.random.randint(0, 9, (3, 3))
print("배열 a:", a)
print("\n배열 a[:, 0]:", a[:, 0])

a[:, 0] = 999

print("\n슬라이싱으로 배열 바꾼 결과:", a)

copied_a = np.copy(a)

print("\ncopy a:", copied_a)
print("\ncopied_a[:, 1]:", copied_a[:, 1])

copied_a[:, 1] = 777

print("\ncopy a:", copied_a)
print("\n배열 a:", a)