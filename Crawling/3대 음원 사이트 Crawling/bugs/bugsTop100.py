# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:26:16 2022

@author: asna9
음원 사이트 crawling
bugs top100 긁고, 파일에 저장.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

musicChart = []

targetSite = "https://music.bugs.co.kr/chart"
request = requests.get(targetSite)
html = request.text
soup = BeautifulSoup(html, "html.parser")

top100s = soup.findAll("p", {"class", "title"})
artists = soup.findAll("p", {"class", "artist"})

for i in range(len(top100s)):
    print(i)
    music = [top100s[i].text.strip(), artists[i].text.strip().split('\n')[0]]
    musicChart.append(music)

"""i=0
print(dt.now())
for music, artist in musicChart:
    print("%d위. %s - %s" %(i+1, music, artist))
    i += 1"""
    
#크롤링한 결과를 텍스트 파일에 저장
file = open('bugs100.txt', 'w', -1, 'UTF-8')

file.write('현재 Bugs 뮤직 실시간 Top 100\n'.format(dt.now()))
for i in range(len(top100s)):
    title, artist = musicChart[i]
    data = '{0:3d}위 {1} - {2}'.format(i+1, title, artist)
    file.write(data+"\n")
file.close()

print("bugs100.txt에 실시간 Top100 저장완료")