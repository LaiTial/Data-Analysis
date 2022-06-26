# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:58:29 2022

@author: asna9

#index, values 속성과 keys() 메소드 test
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

row = scientists.loc['William Sealy Gosset']

# index : 시리즈의 index(열 name)
print("Index:",row.index)

# values : 시리즈의 Data
print("Data:",row.values)

# keys() : index 같이 시리즈의 index
print("Keys:",row.keys())

# index 속성의 첫 번째 값 추출
print("\nFirst index:",row.index[0])
print("First key:",row.keys()[0])

# values 속성의 첫 번째 값 추출하기
print("First value:",row.values[0])