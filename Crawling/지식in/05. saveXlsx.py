"""
[네이버 지식인 크롤링]
https://kin.naver.com/

특정 키워드 검색 후,
*5단계 - 크롤링한 데이터 엑셀 추가
"""

import requests
from bs4 import BeautifulSoup
import openpyxl

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
    
        knowIn["Q"+str(num)] = tempL
        
        num += 1

# xlsx 시트 open
wb = openpyxl.Workbook()
ws = wb.create_sheet("지식in save")

# 데이터 추가
ws['A1'] = 'Num'
ws['B1'], ws['C1'], ws['D1'], ws['E1'] = nameTag

i = 2

for title, contents in knowIn.items():
    ws['A'+str(i)] = i-1
    ws['B'+str(i)], ws['C'+str(i)], ws['D'+str(i)], ws['E'+str(i)] = contents
    
    i += 1
    
wb.save("지식in.xlsx")
