"""
chrome driver
검색창 선택
검색어 보내고 Enter

method chaining이 안되니 유의하자
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #드라이버가 특정 키를 입력하게 만들때 사용
import time

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get("https://www.naver.com/")
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(15) #드라이버 구동 후 n초 동안 기다린다.

#검색창에 검색어 입력
search = driver.find_element(By.CSS_SELECTOR, '#query')
search.send_keys('에어컨') #에어컨이란 검색어를 보낸다
search.send_keys(Keys.ENTER) #검색창 Enter


