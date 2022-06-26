# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:39:38 2022

@author: asna9

데이터 불러오고, 확인.
그리고 불필요한 컬럼을 삭제하고 적절한 자료형으로 변환, 결측치를 분석한다.
"""
import pandas as pd

def dataSet():

    df = pd.read_csv("서울시 코로나19 확진자 현황.csv")

    #1. 컬럼별 데이터 확인
    df['환자번호'].unique() #NaN, '국적', '환자정보', '조치사항', '이동경로'도 NaN

    #2. 불필요한 컬럼 삭제
    df = df.drop(columns=['환자번호', '국적', '환자정보', '조치사항', '이동경로', '등록일', '수정일', '노출여부']) #Nan, 그밖에 불필요한 컬럼 삭제

    #3. 자료형 변환
    # df.dtypes => 자료형 확인, 각기 자료들에 어울리는 자료형으로 변환!
    df['확진일'] = pd.to_datetime(df['확진일'])

    # df['지역'] => '성북구 ', '성북구'식의 ' '로 나누어진 그룹 하나로 통합&정리
    df['지역'] = df['지역'].str.strip() #지역의 공백 제거
    df['지역'] = df['지역'].astype('category') #category형으로 형변환
    #category형 데이터에 문자열 함수를 적용하면 object형으로 돌아가니 주의!

    #4. 결측치 분석
    # df.isnull.sum() => 여행력에만 Null
    
    return df
