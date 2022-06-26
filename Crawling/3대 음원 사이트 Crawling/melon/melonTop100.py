# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:09:32 2022

@author: asna9
멜론차트 Top100 crawling

크롤링시 406 에러가 발생될 경우 헤더 정보 사이트 => https://developers.whatismybrowser.com/useragents/explore/layout_engine_name/trident/
header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

musicChart = []

targetSite = "https://www.melon.com/chart/"

#인터넷 익스플로러 문제가 발생, 브라우저 지정해주는것
header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
request = requests.get(targetSite, headers=header) # <Response [406]> => 헤더 문제로 사이트의 요청한 정보를 얻어올 수 없다.
html = request.text
soup = BeautifulSoup(html, "html.parser")

top100s = soup.findAll("div", {"class", "ellipsis rank01"})
artists = soup.findAll("span", {"class", "checkEllipsis"})

for i in range(len(top100s)):
    music = [top100s[i].text.strip().split('\n')[0], artists[i].text.strip().split('\n')[0]]
    musicChart.append(music)

  
#크롤링한 결과를 텍스트 파일에 저장
file = open('melon100.txt', 'w', -1, 'UTF-8')

file.write('현재 Melon 뮤직 실시간 Top 100\n'.format(dt.now()))
for i in range(len(top100s)):
    title, artist = musicChart[i]
    data = '{0:3d}위. {1} - {2}'.format(i+1, title, artist)
    file.write(data+"\n")
file.close()

print("melon100.txt에 실시간 Top100 저장완료")