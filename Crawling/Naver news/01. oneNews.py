"삼성전자 첫번째 기사 title, text 가져오기"

import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# select_one 선택자와 매칭되는 첫번째 객체 반환
gettitle = soup.select_one('.news_tit') #첫번째 기사의 제목
title = gettitle['title']

contents = soup.select_one('.dsc_txt_wrap') #첫번째 기사의 본문
texts = contents.text

