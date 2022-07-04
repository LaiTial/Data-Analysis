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

#for question in Qs:
title = soup.select_one('._searchListTitleAnchor').text #제목
link = soup.select_one('._searchListTitleAnchor').attrs['href'] #링크
        
date = soup.select_one('.txt_inline').text # 날짜
content = soup.select_one('.txt_inline+dd').text # 내용 #dd:nth-of-type(2) dd:nth-of-child(3) 가능
    
print(title, date, content, link, sep='\n')

