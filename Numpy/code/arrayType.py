# -*- coding: utf-8 -*-
"""
약속된 난수를 생성, 만든 배열의 속성을 확인

@author: asna9
"""

import numpy as np

# 약속된 난수 생성
np.random.seed(100)
arr = np.random.random((2, 3, 6))

# numpy 배열 객체의 속성 확인
print('배열의 타입 : {}'.format(type(arr)))
print('배열의 shape : {}'.format(arr.shape))
print('배열의 길이(면) : {}'.format(len(arr)))
print('배열의 길이(행) : {}'.format(len(arr[0])))
print('배열의 길이(열) : {}'.format(len(arr[0][0])))
print('배열의 차원 : {}'.format(arr.ndim))
print('배열의 요소의 개수 : {}'.format(arr.size))
print('배열의 저장된 데이터 타입 : {}'.format(arr.dtype))
print('배열의 저장된 데이터 타입 이름 : {}'.format(arr.dtype.name))

# 배열의 요소를 정수(int)로 반환한다. => 실제 값이 변환되지는 않고 화면에 보여주기만 한다.
print(arr.astype(np.int32))
print(arr)

#요렇게 하면 배열이 변한다.
arr = arr.astype(np.int64)
print(arr)