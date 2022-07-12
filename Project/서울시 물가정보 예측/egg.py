# -*- coding: utf-8 -*-
"""
달걀 가격 분석
조건 : 달걀의 최근 가격, 기준은 30개, 가격은 0원 이상

1. 달걀의 평균/최고/최저 가격
2. 2만원 이하인 가게는?
3. 각 동네별 달걀 가격을 시각화
4. 마트지점별 달걀 가격을 시각화
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'gulim'

df = pd.read_csv("생필품 농수축산물 가격 정보.csv", encoding='cp949')

# 달걀의 최근 가격, 기준은 30개으로!
df_egg = df[(df['품목 이름'].str.contains('달걀')) & (df['년도-월']=='2021-06') & (df['실판매규격'].str.contains('30개')) & (df['가격(원)'] > 0)]
            
# 달걀 600g의 평균 가격
means = df_egg['가격(원)'].mean()

# 삼겹살 600g의 최고 가격
maxs = df_egg['가격(원)'].max()

# 삼겹살 600g의 최저 가격
mins = df_egg['가격(원)'].min()

# 삼겹살 600g의 최저 가격
store = df_egg[df_egg['가격(원)'] > 20000]
#-------------------------------------------------------------------------------------------
# 우리 동네 달걀 가격
# 구 입력받기
gu = input("구 이름 : ")

# 우리 구 달걀 가격
my_gu = df_egg[df_egg['자치구 이름']==gu][['시장/마트 이름', '품목 이름', '실판매규격', '가격(원)']].drop_duplicates()

# 시각화
print(my_gu.sort_values('가격(원)'))
x, y = my_gu['시장/마트 이름'], my_gu['가격(원)']
plt.title(gu+" 달걀(30구) 가격")
plt.scatter(x, y)
plt.show()

#-------------------------------------------------------------------------------------------
# 마트지점별 달걀 가격

market = input("시장/마트 이름 : ")

# 마트 지점별 삼겹살 가격
df_egg_mart = df_egg[df_egg['시장/마트 이름'].str.contains(market)][['시장/마트 이름', '품목 이름', '실판매규격', '가격(원)']].drop_duplicates()

# 시각화
x, y = df_egg_mart['시장/마트 이름'], df_egg_mart['가격(원)']
plt.title(market+" 달걀(30구) 가격")
plt.scatter(x, y)
plt.xticks(rotation=45)
plt.show()