"""
[네이버 지식인 크롤링]
https://kin.naver.com/

특정 키워드 검색 후,
*3단계 - 1~n 페이지까지 전체 질문의 제목, 날짜, 설명, 링크
(n은 사용자로부터 입력)
"""

import requests
from bs4 import BeautifulSoup


pageNum = int(input("How much page? "))

targetSite="https://kin.naver.com/search/list.naver?query=python&page="
nameTag = ['Date', 'Contents', 'Link']
knowIn = {}

for i in range(1, pageNum+1):
    response = requests.get(targetSite+str(i))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # 지식인 list를 가져온다
    Q = soup.select_one('.basic1')
    
    #for question in Qs:
    getQs = Q.select('dt > a') #제목, 링크
    getConts = Q.select('li') # 날짜, 내용
    
    # 제목과 링크
    for getQ, getCont in zip(getQs, getConts):
        title = getQ.text
        link = getQ.get('href')
    
        tempL = [link]
        
        content = getCont.select('dd') # 날짜, 내용
        
        # dd 태그를 선회하면서 날짜와 본문내용을 얻어온다
        tempL.insert(0, content[0].text)
        tempL.insert(1, content[1].text)
    
        knowIn[title] = tempL
    
# crawling 결과를 출력
for title, contents in knowIn.items():
    print(f"[{title}]\n")
        
    for i in range(3):
        print(nameTag[i]+":",contents[i])
    print("\n\n")