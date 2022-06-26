# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:27:53 2022

@author: asna9

survey_person.csv => 관측한 사람
survey_site.csv => 관측 위치
survey_survey.csv => 날씨 정보, 
survey_visited.csv => 관측 날짜
"""

import numpy as np
import pandas as pd

person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')

# site, visit merge
print("site-visit merge")
o2o_merge = site.merge(visited, left_on='name', right_on='site')
print(o2o_merge)
print("="*80)

# person, survey merge
print("person-survey merge")
p2s_merge = person.merge(survey, left_on='ident', right_on='person')
print(p2s_merge)
print("="*80)

#visited, survey merge
print("visited-survey merge")
v2s_merge = visited.merge(survey, left_on='ident', right_on='taken')
print(v2s_merge)
print("="*80)

# 여러 열을 축으로 dataframe 결합
p2s_v2s_merge = p2s_merge.merge(v2s_merge, left_on=['ident', 'taken', 'quant', 'reading'], \
                               right_on=['person', 'ident', 'quant', 'reading'])
print("여러 열을 축으로 dataframe 결합")
print(p2s_v2s_merge)