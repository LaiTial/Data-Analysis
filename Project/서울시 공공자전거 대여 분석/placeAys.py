# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:42:38 2022

@author: asna9
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt

#전처리된 데이터를 받는다.
df = dS()

#반납대여소번호 오류 처리
df['반납대여소번호'] = df['반납대여소번호'].astype('str') #str형으로 변환
df['반납대여소번호'] = df['반납대여소번호'].str.lstrip('0') #0처리
df['반납대여소번호'] = df['반납대여소번호'].astype('int') #int형으로 변환
df['반납대여소번호'] = df['반납대여소번호'].astype('category') #category형으로 변환

#대여건수가 가장 많은 대여소 best10
df[['대여 대여소번호', '대여 대여소명']].value_counts()[:10]

#반납건수가 가장 많은 대여소 best10
df[['반납대여소번호', '반납대여소명']].value_counts()[:10]

#여의나루역 1번 출구 앞 대여소 이용현황
#서브셋 만들기
df207 = df[df['대여 대여소번호'] == 207]

#반납 현황
df207[['반납대여소번호', '반납대여소명']].value_counts()[:10]

#요일별 대여현황
df207['대여요일'] = df207['대여일시'].dt.strftime('%a') #대여요일 컬럼 추가
df207['대여요일'].value_counts()[:10]

#이용시간 통계
df207['이용시간'].mean() #이용시간 평균
df207['이용시간'].max() #이용시간 최대
df207['이용시간'].min() #이용시간 최소

#전체데이터 이용시간 평균
df['이용시간'].mean()
