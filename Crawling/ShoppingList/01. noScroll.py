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

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get("https://search.shopping.naver.com/search/all?query=%EC%9E%A0%EC%98%B7")
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(20) #드라이버 구동 후 n초 동안 기다린다.

print("\n")

# 컨테이너
infos = driver.find_elements(By.CSS_SELECTOR, "li.basicList_item__2XT81")

for info in infos:
    productN = info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN').text.strip() #상품명
    link = info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN').get_attribute('href') #상세페이지 링크
    price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text.strip() #가격
       
    print(productN, price, link, sep='\n')
    print("\n")

    
