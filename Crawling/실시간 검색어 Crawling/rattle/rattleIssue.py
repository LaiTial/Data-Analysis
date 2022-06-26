# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:35:57 2022

@author: asna9
https://www.rattle.social/
실시간 이슈 10위가 나와있는 사이트 - 래틀 크롤링
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
driver.get('https://www.rattle.social/')

# html 문서를 얻어온다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

ranks = soup.findAll('span', {'class': 'rank'})
issues = soup.findAll('span', {'class': 'text'})

for i in range(10):
    rank, issue = ranks[i+1].text, issues[i+1].text
    print('{0:>2s}위: {1}'.format(rank, issue))

