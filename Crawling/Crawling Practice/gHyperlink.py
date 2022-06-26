# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:24:59 2022

@author: asna9
하이퍼링크들 text를 crawling.

https://basicenglishspeaking.com/daily-english-conversation-topics/
"""
import requests
from bs4 import BeautifulSoup

targetSite = "https://basicenglishspeaking.com/daily-english-conversation-topics/"
request = requests.get(targetSite)
html = request.text
soup = BeautifulSoup(html, "html.parser")

subject = []
divs = soup.findAll('div', {'class', 'tcb-col'})

for div in divs:
    chapters = div.findAll('a')
    
    for chapter in chapters:
        subject.append(chapter.text)
        
for i in range(len(subject)):
    print("{0:2d}. {1}".format(i+1, subject[i]))