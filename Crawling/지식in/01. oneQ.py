"""
[네이버 지식인 크롤링]
https://kin.naver.com/

특정 키워드 검색 후,
*1단계 - 1페이지 첫번째 질문의 제목, 날짜, 설명, 링크
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://kin.naver.com/search/list.naver?query=python")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

knowIn = {}
nameTag = ['Date', 'Contents', 'Link']

# 지식인 list를 가져온다
Q = soup.select_one('.basic1')

#for question in Q:
getQ = Q.select_one('dt > a') #제목, 링크
getCont = Q.select('dd') # 날짜, 내용

# 제목과 링크
title = getQ.text
link = getQ.get('href')

tempL = [link]

# 날짜와 본문내용을 얻어온다
tempL.insert(0, getCont[0].text)
tempL.insert(1, getCont[1].text)

knowIn[title] = tempL

for title, contents in knowIn.items():
    print(f"[{title}]\n")
    
    for i in range(3):
        print(nameTag[i]+":",contents[i])
