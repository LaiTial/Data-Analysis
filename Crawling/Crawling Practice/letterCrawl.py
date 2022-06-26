# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:38:33 2022

@author: asna9
html 속성과 태그에 지정한 속성으로 크롤링하기
"""

import requests
from bs4 import BeautifulSoup

targetSite = "http://www.dowellcomputer.com/main.jsp"
request = requests.get(targetSite)

#print(request)
#<Response [200]> 사이트 정보를 정상적으로 얻어왔다.

html = request.text
soup = BeautifulSoup(html, "html.parser")
notices = soup.findAll("b")

for getText in notices:
    print(getText.text)
    
print("\n")
    
notices = soup.findAll("td", {"class", "tail"})

for getText in notices:
    print(getText.text)