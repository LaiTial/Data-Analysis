# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:22:36 2022

@author: asna9

불린 인덱싱
배열에서 요소의 값이 짝수인 요소의 총 합계를 불린 인덱싱으로 구한다.
"""

import numpy as np

a = np.arange(24).reshape(4, 6)
print("array a:", a, end='\n\n')

# numpy의 브로드캐스팅 기능을 이용해서 짝수인 배열의 요소를 확인!
even_arr = a % 2
print("array even_arr:",even_arr, end='\n\n')

# 짝수인 값만 true, false로 나오게 한다.
even_arr1 = a % 2 == 0
print("array even_arr1:",even_arr1, end='\n\n')

# 불린 인덱싱을 이용하면 True에 해당되는 요소들만 인덱싱.
# a%2==0까지가 브로드캐스팅이고, 이걸 조건으로 삼아 불린 인덱싱을 한것!

print("a[a%2==0]", a[a % 2 == 0])
print("a[even_arr1]", a[even_arr1], end='\n\n')

print("all result:", np.sum(a))
print("even Num:", np.sum(a[a % 2 == 0]))
print("odd Num:", np.sum(a[a % 2 == 1]))