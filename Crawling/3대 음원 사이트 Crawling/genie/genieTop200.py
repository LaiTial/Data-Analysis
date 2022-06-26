# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:02:34 2022

@author: asna9
지니뮤직 top200.
4페이지에 걸쳐서 50곡씩 나와있으며, 크롤링이 끝나기 전에 정보 요청하면 안되므로 주의.
"""

from datetime import datetime as dt
import time
import getMusic as getM
import readWrite as rW

musicChart = []

sPage = "https://www.genie.co.kr/chart/top200"

pageLinked = getM.getHref(sPage)

for i in range(len(pageLinked)):
    time.sleep(1)
    getM.Top50(sPage+pageLinked[i], musicChart)
  

rW.writeGenie(musicChart)

