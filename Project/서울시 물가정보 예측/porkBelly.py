# -*- coding: utf-8 -*-
"""
삽겹살 가격 분석
조건 : 삼겹살의 최근 가격, 기준은 600g

1. 삼겹살의 평균/최고/최저 가격
2. 5000 이하인 가게는?
3. 각 동네별 삼겹살 가격을 시각화
4. 마트지점별 삼갑셜 가격을 시각화
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'gulim'

df = pd.read_csv("생필품 농수축산물 가격 정보.csv", encoding='cp949')

# 삼겹살의 최근 가격, 기준은 600g으로!
df_sam = df[(df['품목 이름'].str.contains('삼겹살')) & (df['년도-월']=='2021-06') & (df['실판매규격'].str.contains('600g'))]

# 삼겹살 600g의 평균 가격
means = df_sam['가격(원)'].mean()

# 삼겹살 600g의 최고 가격
maxs = df_sam['가격(원)'].max()

# 삼겹살 600g의 최저 가격
mins = df_sam['가격(원)'].min()

# 삼겹살 600g의 최저 가격
store = df_sam[df_sam['가격(원)'] < 5000]

#-------------------------------------------------------------------------------------------
# 우리 동네 삼겹살 가격
# 구 입력받기
gu = input("구 이름 : ")

# 우리 구 삼겹살 가격
my_gu = df_sam[df_sam['자치구 이름']==gu][['시장/마트 이름', '품목 이름', '실판매규격', '가격(원)']].drop_duplicates()

# 시각화
x, y = my_gu['시장/마트 이름'], my_gu['가격(원)']
plt.title(gu+" 삼겹살 가격")
plt.scatter(x, y)
plt.grid=True
plt.show()

#-------------------------------------------------------------------------------------------
# 마트지점별 삼겹살 가격

market = input("시장/마트 이름 : ")

# 마트 지점별 삼겹살 가격
df_sam_mart = df_sam[df_sam['시장/마트 이름'].str.contains(market)][['시장/마트 이름', '품목 이름', '실판매규격', '가격(원)']].drop_duplicates()

# 시각화
x, y = df_sam_mart['시장/마트 이름'], df_sam_mart['가격(원)']
plt.title(market+" 삼겹살 가격")
plt.scatter(x, y)
plt.grid=True
plt.xticks(rotation=45)
plt.show()