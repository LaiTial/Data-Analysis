# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:13:19 2022

@author: asna9

numpy가 제공하는 vector 연산 연습
time 메소드로 시간 계산
"""

import numpy as np
import time

a = np.arange(10000000, dtype=np.int64)

now = time.time()

result = 0
for i in a:
    result += i
    
print("for문 돌렸을때 걸린 시간:",time.time()-now)

now = time.time()
result = np.sum(a)
print("sum() 사용시 걸린 시간:",time.time()-now)