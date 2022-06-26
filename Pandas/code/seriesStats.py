# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:30:21 2022

@author: asna9

데이터를 읽어서
통계 메소드로 통계내고, 불린 인덱싱
"""

import pandas as pd

scientists = pd.read_csv('../data/scientists.csv')

ages = scientists['Age']

# 기초 통계
print('max = {}'.format(ages.max()))
print('min = {}'.format(ages.min()))
print('sum = {}'.format(ages.sum()))
print('mean = {}'.format(ages.mean()))
print('std = {}\n'.format(ages.std()))

# 평균 나이보다 나이가 많은 사람의 데이터를 추출
print("[평균보다 나이가 많은 사람]")
print(ages[ages > ages.mean()]) #ages > ages.mean() => bool 값
