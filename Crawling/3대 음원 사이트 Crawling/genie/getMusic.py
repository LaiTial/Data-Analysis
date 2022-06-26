# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:48:08 2022

@author: asna9
음원 순위가 나와있는 4개의 페이지의 주소를 가져오는 함수 getHref.
각 사이트의 주소를 받아 Top50씩 가져오는 함수 Top50.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
import time

#음원 순위 가져오기
def Top50(targetSite, musicChart):
    header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = requests.get(targetSite, headers=header) # <Response [406]> => 헤더 문제로 사이트의 요청한 정보를 얻어올 수 없다.
    html = request.text
    soup = BeautifulSoup(html, "html.parser")
    
    top100s = soup.findAll("a", {"class", "title ellipsis"})
    artists = soup.findAll("a", {"class", "artist ellipsis"})
    
    
    for i in range(len(top100s)):
        music = [top100s[i].text.strip().split('\n')[0], artists[i+5].text.strip().split('\n')[0]]
        musicChart.append(music)

#타켓 사이트 주소 가져오기
def getHref(sPage):
    
    pageLinked = []
    
    header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = requests.get(sPage, headers=header) # <Response [406]> => 헤더 문제로 사이트의 요청한 정보를 얻어올 수 없다.
    html = request.text
    soup = BeautifulSoup(html, "html.parser")
    
    pageMoves = soup.findAll("div", {"class", "page-nav rank-page-nav"})
    
    for pageMove in pageMoves:
        linked = pageMove.findAll('a')
        
        for link in linked:
            pageLinked.append(link.get('href'))
            
    return pageLinked

