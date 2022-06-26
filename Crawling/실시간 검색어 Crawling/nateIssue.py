# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:20:40 2022

@author: asna9
네이트 실시간 이슈 키워드 crawling
-문제 : 실시간 검색어가 1~5, 혹은 6~10위만 나온다.
"""

import requests
from bs4 import BeautifulSoup

targetSite = "https://www.nate.com/"
request = requests.get(targetSite)
html = request.text
soup = BeautifulSoup(html, "html.parser")

ranks = soup.findAll('span', {'class': 'num_rank'})
issues = soup.findAll('a', {'class': 'ik'})

for i in range(5):
    rank = ranks[i].text
    
    issue = issues[i].text.strip().split('\n')[0]
    upDown = issues[i].text.strip().split('\n')[1]
    
    print('{0:>2s}위: {1}'.format(rank, issue), end='')
    
    if upDown[:2] == '상승':
        print('[{}{}]'.format('↑', upDown[2:]))
        
    elif upDown[:2] == '하락':
        print('[{}{}]'.format('↓', upDown[2:]))
        
    elif upDown[:2] == '동일':
        print('[-]')
        
    else:
        print('[new]')