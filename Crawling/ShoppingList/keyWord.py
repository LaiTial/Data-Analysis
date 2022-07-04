"""
chrome driver
쇼핑 crawling

3단계 : 검색어 처리
상품명, 가격, 상세페이지 링크
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #드라이버가 특정 키를 입력하게 만들때 사용
import time

targetsite = "https://search.shopping.naver.com/search/all?query="

keyword = input("keyword? ")

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get(targetsite+keyword)
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(20) #드라이버 구동 후 n초 동안 기다린다.

# 스크롤 내린다
driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END) # 맨 밑까지 스크롤을 내린다.
time.sleep(1) #잠깐의 텀을 둔다


print("\n")

# 컨테이너
infos = driver.find_elements(By.CSS_SELECTOR, "li.basicList_item__2XT81")

for info in infos:
    productN = info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN').text.strip() #상품명
    link = info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN').get_attribute('href') #상세페이지 링크
    price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn').text.strip() #가격
       
    print(productN, price, link, sep='\n')
    print("\n")

    