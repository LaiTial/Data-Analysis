"""
[네이버 지식인 크롤링]
https://kin.naver.com/

특정 키워드 검색 후,
*4단계 - 검색 키워드 변경 (검색어를 사용자로부터 입력)
"""

import requests
from bs4 import BeautifulSoup

keyword = input("keyword? ")
pageNum = int(input("How much page? "))

targetSite="https://kin.naver.com/search/list.naver?query=" + keyword + "&page="
nameTag = ['Question', 'Date', 'Contents', 'Link']
knowIn = {}

# 문제 번호
num = 1

for i in range(1, pageNum+1):
    response = requests.get(targetSite+str(i))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # 지식인 list를 가져온다
    Q = soup.select('.basic1 > li')
    
    # 제목과 링크
    for lists in Q:
        
        #for question in Qs:
        title = lists.select_one('a').text #제목
        link = lists.select_one('a').attrs['href'] #링크
        
        date = lists.select_one('.txt_inline').text # 날짜
        content = lists.select_one('.txt_inline+dd').text # 내용 #dd:nth-of-type(2) dd:nth-of-child(3) 가능
    
        tempL = [title, date, content, link]
        knowIn["Q"+str(num)] = tempL
        
        num += 1
    
    
# crawling 결과를 출력
for title, contents in knowIn.items():
    print(f"[{title}]\n")
    
    for i in range(4):
        print(nameTag[i]+":",contents[i])
    print("\n\n")
