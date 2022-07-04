"""
chrome driver에서
login 버튼 클릭
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get("https://www.naver.com/")
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(15) #드라이버 구동 후 n초 동안 기다린다.

#로그인 버튼 찾는다.
login = driver.find_element(By.CSS_SELECTOR, '.link_login')
login.click() #click


