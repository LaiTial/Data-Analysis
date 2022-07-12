# -*- coding: utf-8 -*-
"""
강남역 승하차정보 분석
이전 분석 결과에서 가장 많이 붐비는 역이 강남이라 강남 선택!
시간대별 승하차인원 시각화하기
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from dataS import dataSet

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'gulim'

df_in, df_out = dataSet()

#최근 월을 기준으로 한 데이터프레임 생성
df_in08 = df_in[df_in['사용월']=='202108']
df_out08 = df_out[df_out['사용월']=='202108']

#=> 출퇴근시간에 가장 붐비는 역이 강남, 신림역!
#강남역 최근 승하차정보 불러오기
#승차정보
df_gamnam_in = df_in08[df_in08['지하철역']=='강남'].iloc[:,3:] #승차정보
df_gamnam_in = df_gamnam_in.melt() #정리해보기 위해 melt 이용
df_gamnam_in.columns = ['시간대','승차건수'] #컬럼명 변경

#시간대별 승차인원 시각화하기
plt.barh(df_gamnam_in['시간대'], df_gamnam_in['승차건수'], color='skyblue')
plt.show()

#하차정보
df_gamnam_out = df_out08[df_out08['지하철역']=='강남'].iloc[:,3:] #승하차정보
df_gamnam_out = df_gamnam_out.melt() #정리해보기 위해 melt 이용
df_gamnam_out.columns = ['시간대','하차건수'] #컬럼명 변경

#시간대별 하차인원 시각화하기
plt.barh(df_gamnam_out['시간대'], df_gamnam_out['하차건수'], color='pink')
plt.show()