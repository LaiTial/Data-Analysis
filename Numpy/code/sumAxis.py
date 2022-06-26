# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:42:50 2022

@author: asna9
numpy 라이브러리에서 사용하는 Sum()
chart 생성 : https://matplotlib.org/stable/gallery/index
"""

import numpy as np

arr = np.arange(0, 30)
v = arr.reshape(3, 5, 2)

#sum() 함수의 axis 속성의 기본값은 'None'(=기준이 없다)이고, axis는 대상 데이터의 차원보다 작은 값을 설정한다.
#예) 차원이 3이면 axis 속성은 최대 2까지 지정 가능

# axis=None
# axis를 기본값으로 설정하면 대상 데이터의 모든 요소의 합계를 계산.
# 대상 데이터에 포함된 모든 요소를 단순히 합산하는 연산이 실행.
print("<axis=None>")
print("shape: {0}, ndim: {1}".format(v.shape, v.ndim)) #axis 생략 상태
print("sum(): {0}, sum(axis): {1}".format(v.sum(), v.sum(axis=None))) #axis 생략 상태

# axis=0
# axis=0는 데이터의 x축을 기준으로 합계를 계산하고 결과 shape는 면이 제거되고 리턴

# 가장 외곽의 괄호를 제거하는 이미지를 생각하면 된다.
# 괄호를 제거하고 각 행의 데이터는 위치별로 합계를 계산.
r = v.sum(axis=0)
print("\n<axis=0>")
print("shape: {0}, ndim: {1}".format(r.shape, r.ndim)) #3차원->2차원으로 차원 축소
print("sum(axis): \n{0}".format(r))

# axis=1
# axis=1는 y축을 기준으로 합계를 계산하고 결과 shape은 행이 제거되고 리턴
# 가운데 괄호를 제거하는 이미지를 생각하면 된다.
r = v.sum(axis=1)
print("\n<axis=1>")
print("shape: {0}, ndim: {1}".format(r.shape, r.ndim)) #3차원->2차원으로 차원 축소
print("sum(axis): \n{0}".format(r))

# axis=2
# axis=2는 z축을 기준으로 합계를 계산하고 결과 shape은 열이 제거되고 리턴.
# 가장 안쪽 괄호를 제거하는 이미지를 생각하면 된다.
r = v.sum(axis=2)
print("\n<axis=2>")
print("shape: {0}, ndim: {1}".format(r.shape, r.ndim)) #3차원->2차원으로 차원 축소
print("sum(axis): \n{0}".format(r))
