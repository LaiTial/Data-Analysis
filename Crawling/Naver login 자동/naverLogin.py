"""
chrome driver
네이버 로그인 자동화 프로그램
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #드라이버가 특정 키를 입력하게 만들때 사용
import time
import pyperclip
import pyautogui

user_id = 'id명'
user_pw = 'PW명'

driver = webdriver.Chrome('../chromedriver.exe')

# get() 메소드로 가상 크롬에 크롤링할 타겟 사이트를 띄운다.
driver.get("https://www.naver.com/")
driver.maximize_window() #화면을 최대화
driver.implicitly_wait(15) #드라이버 구동 후 n초 동안 기다린다.

#로그인 버튼 찾는다.
login = driver.find_element(By.CSS_SELECTOR, '.link_login')
login.click() #click

#ID, PW 입력
#자동 로그인 방지 풀기
#send_keys()는 robot 검사에 걸릴 수 있으므로 복사해서 붙여넣는 메소드를 대신 사용.
ID = driver.find_element(By.CSS_SELECTOR, '#id')
ID.click()
pyperclip.copy(user_id) #id를 복사
pyautogui.hotkey('ctrl', 'v') #붙여넣기
time.sleep(1) #중간중간 쉬어준다.

PW = driver.find_element(By.CSS_SELECTOR, '#pw')
PW.click()
pyperclip.copy(user_pw) #pw를 복사
pyautogui.hotkey('ctrl', 'v') #붙여넣기
time.sleep(1) #중간중간 쉬어준다.

#로그인 버튼 click
login_btn = driver.find_element(By.CSS_SELECTOR, '.btn_login') #검색창 Enter
login_btn.click()

#기기 등록 여부
enter = driver.find_element(By.CSS_SELECTOR, '.btn') #검색창 Enter
enter.click()

# 기기 등록 여부가 안나올경우를 대비해 naver 원 페이지로 이동
driver.get("https://www.naver.com/")


