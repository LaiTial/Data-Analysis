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
num = 1

# 지식인 list를 가져온다
Q = soup.select('.basic1 > li')
    
# 제목과 링크
for lists in Q:
        
    #for question in Qs:
    title = lists.select_one('._searchListTitleAnchor').text #제목
    link = lists.select_one('._searchListTitleAnchor').attrs['href'] #링크
        
    date = lists.select_one('.txt_inline').text # 날짜
    content = lists.select_one('.txt_inline+dd').text # 내용 #dd:nth-of-type(2) dd:nth-of-child(3) 가능
    
    tempL = [title, date, content, link]
    knowIn["Q"+str(num)] = tempL
        
    num += 1

for title, contents in knowIn.items():
    print(f"[{title}]\n")
    
    for i in range(4):
        print(nameTag[i]+":",contents[i])
    print("\n\n")
