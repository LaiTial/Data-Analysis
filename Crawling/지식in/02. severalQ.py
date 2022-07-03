"""
[네이버 지식인 크롤링]
https://kin.naver.com/

특정 키워드 검색 후,
*2단계 - 1페이지 전체 질문의 제목, 날짜, 설명, 링크
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://kin.naver.com/search/list.naver?query=python")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

knowIn = {}
nameTag = ['Question', 'Date', 'Contents', 'Link']
i = 1

# 지식인 list를 가져온다
Q = soup.select_one('.basic1')

#for question in Qs:
getQs = Q.select('dt > a') #제목, 링크
getConts = Q.select('li') # 날짜, 내용

# 제목과 링크
for getQ, getCont in zip(getQs, getConts):
    title = getQ.text
    link = getQ.get('href')

    tempL = [title, link]
    
    content = getCont.select('dd') # 날짜, 내용
    
    # 날짜와 본문내용을 얻어온다
    tempL.insert(1, content[0].text)
    tempL.insert(2, content[1].text)

    knowIn["Q"+str(i)] = tempL
    
    i += 1

for title, contents in knowIn.items():
    print(f"[{title}]\n")
    
    for i in range(4):
        print(nameTag[i]+":",contents[i])
    print("\n\n")