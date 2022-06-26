# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:53:10 2022

@author: asna9
shape이 같은 두 배열의 연산을 실행
shape이 서로 다른 두 배열의 연산을 실행
- 숫자와 배열의 연산
- shape이 다른 두 배열의 연산
"""

import numpy as np

a = np.arange(1, 25).reshape(4, 6)
b = np.arange(25, 49).reshape(4, 6)

print("a:", a, end='\n\n')
print("b:", b, end='\n\n')

# shape이 같은 두 배열을 이항 연산할 경우 위치가 같은 요소 단위로 실행된다.
print("shape이 같은 두 배열의 연산:",a + b, end='\n\n')

#shape이 다른 두 배열의 연산
#shape이 다른 두 배열의 연산에서 브로드캐스팅 발생 시 두 배열을 같은 shape으로 만든 후 연산을 실행

# case 1 : 배열과 스칼라(단일 값)의 연산
# 배열과 스칼라 사이의 연산 시 스칼라를 배열로 변환
a = np.arange(1, 25).reshape(4, 6)
print("a:", a, end='\n\n')
print("a+100:", a+100, end='\n\n')

# a + 100은 다음과 같은 과정을 거쳐 처리된다.
new_arr = np.full_like(a, 100)
print("new_arr:", new_arr, end='\n\n')
print("a+new_arr:", a + new_arr, end='\n\n')

# case 2 : shape이 다른 배열의 연산
# 데이터를 이렇게 구성하면 반복되기 때문에 잘 사용하지 않는다.
a = np.arange(5).reshape(1, 5)
b = np.arange(5).reshape(5, 1)
print("a:", a, end='\n\n')
print("b:", b, end='\n\n')
print("a+b:", a+b, end='\n\n')