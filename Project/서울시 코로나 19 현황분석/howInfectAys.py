# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:15:49 2022

@author: asna9

감염경로에 따른 확진자수 분석
"""

import pandas as pd
from dataPprocess import dataSet as dS
import matplotlib.pyplot as plt
import matplotlib as mpl

#전처리된 데이터를 받는다.
df = dS()

#접촉력에 따른 확진건수 best10
best10 = df['접촉력'].value_counts()[:10]

#최근월 접촉력에 따른 확진건수 best10
df = df.sort_values(by='확진일')
now10 = df[(df['확진일'].dt.year==2021) & (df['확진일'].dt.month==9)]['접촉력'].value_counts()[:10]


