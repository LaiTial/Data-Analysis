# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:27:46 2022

@author: asna9

numpy의 sort 메소드 test
일반 정렬되지 않은 배열을 아무런 축도 주지 않고 정렬.
axis는 0, 1 각각 줘서 test
"""

import numpy as np

# 원본 배열
unsorted_arr = np.random.randint(1, 10, (3, 3), np.int64)
print("정렬되지 않은 배열:",unsorted_arr)

# sort 작업을 위해 원본을 복사
unsorted_arr1 = unsorted_arr.copy()
unsorted_arr2 = unsorted_arr.copy()
unsorted_arr3 = unsorted_arr.copy()

#배열을 sort.

unsorted_arr1.sort()
print("\n배열 정렬:",unsorted_arr1)

unsorted_arr2.sort(axis=1)
print("\naxis=1을 기준으로 정렬:",unsorted_arr2)

unsorted_arr3.sort(axis=0)
print("\naxis=0을 기준으로 정렬:",unsorted_arr3)
