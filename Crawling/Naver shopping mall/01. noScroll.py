"""
chrome driver
쇼핑 crawling
1단계 : 스크롤 전 크롤링
상품명, 가격, 상세페이지 링크
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #드라이버가 특정 키를 입력하게 만들때 사용
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get("https://search.shopping.naver.com/search/all?query=%EC%9E%A0%EC%98%B7")
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(20) #드라이버 구동 후 n초 동안 기다린다.

# 페이지 소스를 얻어온다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 컨테이너
contentBox = soup.select('.basicList_item__2XT81')

print("\n")

for info in contentBox:
    
    product = info.select_one('.basicList_link__1MaTN') #a 태그 가져온다
    
    productN = product.text.strip() #상품명
    link = product.attrs['href'] #상세페이지 링크
    price = info.select_one('.price_num__2WUXn').text.strip() #가격
    
    try:
        img = info.select_one('.thumbnail_thumb__3Agq6 > img').attrs['src'] #이미지 경로 가져온다
    except:
        continue;
    
    print(productN, price, link, img, sep='\n')
    print("\n")
