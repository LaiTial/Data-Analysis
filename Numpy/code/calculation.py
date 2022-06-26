# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:31:56 2022
배열의 산술 연산 - 덧셈, 뺄셈, 곱셈, 나눗셈
지수연산, 제곱근 연산, 삼각함수, 로그계산, 행렬의 내적계산 결과 출력

비교 연산 - 배열 요소별 비교, 전체 비교
@author: asna9
"""

import numpy as np

# 배열 생성
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(9, 0, -1).reshape(3, 3)

print("배열 a:", a, end='\n\n')
print("배열 b:", b, end='\n\n')

# 덧셈 : +, np.add()
print("a+b:", a + b, end='\n\n')
print("np.add(a, b):", np.add(a, b), end='\n\n')

# 뺄셈 : -, np.subtract()
print("a-b:", a - b, end='\n\n')
print("np.subtract(a, b):", np.subtract(a, b), end='\n\n')

# 곱셈 : *, np.multiply()
print("a*b:", a*b, end='\n\n')
print("np.multiply(a, b):", np.multiply(a, b), end='\n\n')

# 나눗셈 : /, np.divide()
print("a/b:", a/b, end='\n\n')
print("np.divide(a, b):", np.divide(a, b), end='\n\n')

#지수
print("np.exp(a):", np.exp(a), end='\n\n')

#제곱근
print("np.sqrt(a):", np.sqrt(a), end='\n\n')

# 삼각함수
print("np.sin(a):", np.sin(a), end='\n\n')# sin
print("np.cos(a):", np.cos(a), end='\n\n') # cos
print("np.tan(a):", np.tan(a), end='\n\n') # tan
print("np.log(a):", np.log(a), end='\n\n') # log
print("np.dot(a, b):", np.dot(a, b), end='\n\n') # 행렬의 내적

# 배열 요소별 비교 : >, >=, <, <=, ==, !=
print("a == b:", a == b, end='\n\n') 

# np.array_equal() - 배열 전체 비교
print("np.array_equal(a, b):", np.array_equal(a, b), end='\n\n')
