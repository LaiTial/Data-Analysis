# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:28:20 2022

@author: asna9
"""

# 사용자 정의 함수
def my_mean(values):
    n = len(values)
    total = 0
    for value in values:
        total += value
    return total / n

# year 별로 계산된 그룹 평균과 전체 평균의 편차를 계산하는 함수
def my_mean_diff(values, diff_value):
    n = len(values)
    total = 0
    for value in values:
        total += value
    mean = total / n
    # 그룹별 평균에서 전체 평균을 뺀 값을 리턴시킨다.
    return mean - diff_value

# 표준점수 계산하기
def my_zscore(x):
    return (x - x.mean()) / x.std()