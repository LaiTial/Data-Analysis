# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:20:58 2022

@author: asna9

시리즈
기초 통계 메소드 test
"""
import pandas as pd

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

ages = scientists['Age']
print(type(ages), end='\n\n')
print(ages)

print('\nmax = {}'.format(ages.max()))
print('min = {}'.format(ages.min()))
print('sum = {}'.format(ages.sum()))
print('mean = {}'.format(ages.mean()))
print('std = {}'.format(ages.std()))