# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:58:20 2022

@author: asna9

서울시 공공자전거 대여정보 분석.
0~5 파일을 통합, 불필요한 컬럼 삭제하고 적절한 자료형으로 변환하는 등 전처리를 하는 py.
"""

import pandas as pd

def dataSet():
    
    xslx = []
        
    for i in range(6):
        text = "공공자전거 대여이력 정보_2021.0" + str(i+1) + ".csv"
        xslx.append(pd.read_csv(text, encoding = 'cp949', low_memory=(False)))
        
    df = pd.concat(xslx)
    
    #1. 불필요한 컬럼 삭제
    df = df.drop(columns=['자전거번호', '대여거치대', '반납거치대']) 
    
    #2. 자료형 변환
    # df.dtypes => 자료형 확인, 각기 자료들에 어울리는 자료형으로 변환!
    df['대여 대여소번호'] = df['대여 대여소번호'].astype('category')
    df['반납대여소번호'] = df['반납대여소번호'].astype('category')
    
    df['대여일시'] = pd.to_datetime(df['대여일시'], errors='coerce')
    df['반납일시'] = pd.to_datetime(df['반납일시'], errors='coerce')
    
    #3. 결측치 분석
    # df.isnull.sum() => 반납일시, 이용거리에 Null
    df.dropna(inplace=True) #Null이 발생한 자료 삭제

    return df
