# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:47:05 2022

@author: asna9
css로 크롤링하기
자식 선택자(>)랑 하위,자식 선택자를 이용.
select('css 선택자')
"""

import requests
from bs4 import BeautifulSoup

targetSite = "http://www.dowellcomputer.com/main.jsp"
request = requests.get(targetSite)

#print(request)
#<Response [200]> 사이트 정보를 정상적으로 얻어왔다.

html = request.text
soup = BeautifulSoup(html, "html.parser")
notices = soup.select('td > a')

for getText in notices:    
    if('notice' in getText.get('href')):
        print(getText.text)

