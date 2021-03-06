# -*- coding: utf-8 -*-
"""
출퇴근시간 역별 승하차인원 분석
"""

import pandas as pd
from dataS import dataSet

df_in, df_out = dataSet()

#출퇴근시간 역별 승하차인원 분석
#최근 월을 기준으로 한 데이터프레임 생성
df_in08 = df_in[df_in['사용월']=='202108']
df_out08 = df_out[df_out['사용월']=='202108']

#출근시간(08~09시)에 가장 많은 사람이 승차하는 역
intop10s = df_in08.nlargest(10, '08시-09시')[['지하철역', '08시-09시']]

#출근시간(09~10시)에 가장 많은 사람이 하차하는 역
outtop10s = df_out08.nlargest(10, '09시-10시')[['지하철역', '09시-10시']]

#퇴근시간(18~19시)에 가장 많은 사람이 승차하는 역
intop10e = df_in08.nlargest(10, '18시-19시')[['지하철역', '18시-19시']]

#퇴근시간(19~20시)에 가장 많은 사람이 하차하는 역
outtop10e = df_out08.nlargest(10, '19시-20시')[['지하철역', '19시-20시']]