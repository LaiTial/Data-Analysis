# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:43:10 2022

@author: asna9
네이트 실시간 이슈 키워드 crawling

개발자모드->Network->XHR->jsonLiveKeywordDataV1.js?v=202203142240->Preview
"""

import requests
from datetime import datetime as dt
import json

#json 모듈의 loads() 메소드를 사용해 파이썬에서 처리할 수 있게 리스트 or 딕셔너리로 자동변환
#request.text로 얻은 문자열 데이터를 받아 변환
def chJson(chData):
    
    data = json.loads(chData)
    
    return data

targetSite = "https://www.nate.com/js/data/jsonLiveKeywordDataV1.js?v=202203142255"

#Request Method가 GET이므로 request 모듈의 get()을 사용해서 실시간 검색어를 얻어온다.
#브라우저를 사용하지 않기 때문에 header 지정할 필요가 x
request = requests.get(targetSite)

#일반적으로 request.text를 할시, 문자열이 나온다.
#왜냐면 ajax로 처리되는 정보는 무조건 문자열이기 때문!

# json()로 서버에 요청해서 전달받은 데이터를 파이썬에서 처리할 수 있는 리스트나 딕셔너리 타입으로 변환.
# 데이터가 []로 묶여 있으면 리스트, {}로 묶여있으면 딕셔너리로 자동변환.
issueRanks = request.json()

for issueRank in issueRanks:
    rank, issue, upDown, num = issueRank[:4]
    
    print('{0:>2s}위: {1}'.format(rank, issue), end='')
    
    if upDown == '+':
        print('[{}{}]'.format('↑', num))
        
    elif upDown == '-':
        print('[{}{}]'.format('↓', num))
        
    elif upDown == 's':
        print('[-]')
        
    else:
        print('[new]')




