# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:22:27 2022

@author: asna9
한 건의 대화 정보를 저장시키는 클래스 구현
"""

import requests
from bs4 import BeautifulSoup
import time

class Conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return '질문 : {}\n답변 : {}\n'.format(self.question, self.answer)
    
def getSubject():
    targetSite = "https://basicenglishspeaking.com/daily-english-conversation-topics/"
    request = requests.get(targetSite)
    html = request.text
    soup = BeautifulSoup(html, "html.parser")
    
    subject = []
    contentLink = [] #세부 대화 내용의 url를 저장할 빈 리스트
    divs = soup.findAll('div', {'class', 'tcb-col'})
    
    for div in divs:
        chapters = div.findAll('a')
        
        for chapter in chapters:
            subject.append(chapter.text)
            contentLink.append(chapter.get('href')) #url 추가
            
    #대화 내용과, 세부 대화 내용 url를 return
    return subject, contentLink
    

subject, contentLink = getSubject()

#대화 주제에 따른 모든 대화 내용을 저장할 빈 리스트 선언
conversation = [] #Conversation 클래스 객체를 저장
i = 0 #대화 주제를 count, 주제만큼 반복하여 대화 내용을 크롤링

for s in subject[:1]:

    #대화 주제별 크롤링할 페이지를 요청한다.
    request = requests.get(contentLink[i])
    
    #대형 포탈 사이트는 짧은 간격으로 많은 요청이 들어오면 자기네 사이트가 공격당하는 것으로 믿기 때문에 시간 간격을 두는것!
    #페이지가 로딩되는 시간만큼 기다리기 위하여 일정 시간간격을 두고 정보요청.
    time.sleep(1) #프로그램을 1초간 멈춘다
    html = request.text
    soup = BeautifulSoup(html, "html.parser")
    
    #대화 내용은 class 속성이 'sc_player_container1'인 div 태그의 형제.
    divs = soup.findAll('div', {'class', 'sc_player_container1'})
    
    for div in divs:
        
        #index() : 인수로 지정된 객체의 index 번호를 얻어온다.
        #대화 내용 전체(divs)에서 특정 대화(div)의 index 번호를 get
        num = divs.index(div)
        
        #크롤링할 데이터는 이 div 태그의 다음 형제로 작성.
        #next_sibling->다음형제, previous_sibling->이전형제
        
        if (num%2 == 0):
            question = div.next_sibling
        else:
            answer = div.next_sibling
            
            #질문과 답변이 한 쌍이 되었으므로 대화 내용 저장 객체 생성해, 저장
            c = Conversation(question, answer)
            
            #이 객체를 대화 내용을 기억할 conversation 리스트에 저장
            conversation.append(c)
    
    i += 1

for c in conversation:
    print(c)

