# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:56:27 2022

@author: asna9
결과를 받아 출력하는 함수 printChart
크롤링한 결과를 텍스트 파일에 저장하는 함수 writeGenie
"""

from datetime import datetime as dt

#크롤링한 결과를 print
def printChart(musicChart):
    i=0
    print(dt.now())
    for music, artist in musicChart:
        print("%d위. %s - %s" %(i+1, music, artist))
        i += 1

#크롤링한 결과를 텍스트 파일에 저장
def writeGenie(musicChart):
    #인코딩 오류를 방지하고자 지정
    file = open('genie200.txt', 'w', -1, 'UTF-8')

    file.write('현재 Genie 뮤직 실시간 Top 200\n'.format(dt.now()))
    for i in range(len(musicChart)):
        title, artist = musicChart[i]
        data = '{0:3d}위. {1} - {2}'.format(i+1, title, artist)
        file.write(data+"\n")
    file.close()

    print("genie200.txt에 실시간 Top100 저장완료")
