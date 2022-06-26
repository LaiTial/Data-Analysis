# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:53:08 2022

@author: asna9
"""

import numpy as np

# 데모 배열 객체 생성
data = np.random.random((3, 4))
print(data)

# 배열 객체 저장 - 텍스트 파일
np.savetxt('../output/saved.csv', data, delimiter=',')
np.savetxt('../output/saved.tsv', data, delimiter='\t')

# np.loadtxt('파일명', dtype, delimiter='구분자')
print(np.loadtxt('../output/saved.csv', dtype=float, delimiter=','))
