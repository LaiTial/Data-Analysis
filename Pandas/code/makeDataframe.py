# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:32:43 2022

@author: asna9
"""

import pandas as pd

# 기본 데이터프레임 생성
scientists = pd.DataFrame({
    'Name': ['Rosaline Ftanklin', 'William Sealy Gosset'],
    'Occupation': ['Chemist', 'Statistcian'],
    'Born': ['1920-04-20', '1875-06-10'],
    'Died': ['1957-08-20', '1930-12-10'],
    'Age': [37, 60]
})
print(scientists, end='\n\n')

# data 속성, index 속성, columns 속성으로 데이터프레임 생성
scientists = pd.DataFrame(
    data={
        'Occupation': ['Chemist', 'Statistcian'],
        'Born': ['1920-04-20', '1875-06-10'],
        'Died': ['1957-08-20', '1930-12-10'],
        'Age': [37, 60]
    },
    index=['Rosaline Ftanklin', 'William Sealy Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age']
)
print(scientists, end='\n\n')

# 순서를 보장하는 데이터 프레임 생성
from collections import OrderedDict
scientists = pd.DataFrame(
    OrderedDict([
        ('Name', ['Rosaline Ftanklin', 'William Sealy Gosset']),
        ('Occupation', ['Chemist', 'Statistcian']),
        ('Born', ['1920-04-20', '1875-06-10']),
        ('Died', ['1957-08-20', '1930-12-10']),
        ('Age', [37, 60])
    ])
)
print(scientists, end='\n\n')