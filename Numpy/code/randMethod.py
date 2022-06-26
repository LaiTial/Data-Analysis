# -*- coding: utf-8 -*-
"""
numpy의 난수생성 함수 5개로 난수를 생성, 
time으로 시간간격을 주어 하나씩 보여준다.

10000개의 결과를 100개의 구간으로 구분한 히스토그램 차트로!
@author: asna9
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def mHist(data, bins, title):
    plt.hist(data, bins=bins)
    plt.title(title, fontsize=13)
    plt.show()
    
    time.sleep(2)

#random.normal(loc, scale, size)
# loc => 정규 분포의 평균, scale => 표준편차, size => 행렬의 크기, 난수의 개수
mean = 10
std = 2

data = np.random.normal(mean, std, 10000)
mHist(data, 100, 'normal')

# np.random.randn(d0, d1, ..., dn)
data = np.random.randn(10000)
mHist(data, 100, 'randn')

# np.random.rand(d0, d1, ..., dn)
data = np.random.rand(10000)
mHist(data, 10, 'rand')

# np.random.randint(low, high, size)
data = np.random.randint(-100, 100, 10000)
mHist(data, 10, 'randint')

# np.random.random(size)
data = np.random.random(10000)
mHist(data, 10, 'random')