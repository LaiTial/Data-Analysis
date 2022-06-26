# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:01:17 2022

@author: asna9
"""

import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver

# selenium을 사용해서 가상 크롬을 실행.
# 사용중인 크롬 버전과 같은 버전의 크롬 드라이버를 OS에 맞게 다운받고,
# 다운받은 크롬 드라이버를 현재 소스파일이 위치한 경로에 복사해 넣고 사용.
driver = webdriver.Chrome('D:/Python/Crawling/chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get('https://www.nate.com/')

# html 문서를 얻어온다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

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