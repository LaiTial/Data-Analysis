# -*- coding: utf-8 -*-
"""
데이터 전처리 하는 파일
결측치 확인하고 적절한 데이터 타입으로 변환, 불필요한 컬럼을 삭제한다.

그리고 하나로 되어있는 승하차 테이블을 분리해 승차 테이블, 하차테이블로 만든다.
"""

import pandas as pd

def dataSet():

    df = pd.read_csv("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding='cp949')
    
    #1. 결측치 확인
    df.isnull().sum() #=> 없음!
    
    #2. 데이터 타입 변환
    df['사용월'] = df['사용월'].astype('str')
    
    #3. 불필요한 컬럼 삭제
    df.drop(columns='작업일자', inplace=True)
    
    #승차, 하차 테이블 분리
    
    #승차 테이블 만들기
    df_init = df.iloc[:,:3] #공통 컬럼 분리
    df_s = df.iloc[:,3::2] #승차 컬럼만 가져오기
    df_s.columns = df_s.columns.str.split().str[0] #컬럼명 변경. '시간 승차인원' -> '시간'으로!
    
    #공통컬럼과 승차컬럼 연결하기
    df_in = pd.concat([df_init, df_s], axis=1)
    
    #하차 테이블 만들기
    df_h = df.iloc[:,4::2] #하차 컬럼만 가져오기
    df_h.columns = df_h.columns.str.split().str[0] #컬럼명 변경. '시간 하차인원' -> '시간'으로!
    
    #공통컬럼과 하차컬럼 연결하기
    df_out = pd.concat([df_init, df_h], axis=1)
    
    return df_in, df_out

