# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:42:44 2022

@author: asna9
"""

from bs4 import BeautifulSoup
 
html_doc = """
<table border=1> 
  <tr>     
     <th id = "choco">초콜릿</th>    
     <th id = "cookie">과자</th>  
  </tr>  
  <tr>    
     <td name = "candy">사탕</td>
     <td>오렌지</td>
  </tr>  
</table>
"""
 
# html 파서를 이용해서 html 형태의 데이터를 읽어온다.
soup = BeautifulSoup(html_doc, 'html.parser')
 
# 1. td 태그를 모두 찾아서 td_list 담은 후, 루프를 돌리면서 각 td 태그 내용을 출력한다.
td_list = soup.find_all('td')
for td_item in td_list:
  print(td_item.string)
 
print ('\n')
 
# 2. id 가 choco 인 항목을 찾아서 해당 태그 내용을 출력한다. 
id_list = soup.find(id='choco')
print(id_list.string)
 
# 3. td 태그이면서 name 속성이 candy 인 항목('캔디')을 찾아서 
#    그 다음에 있는 같은 td 속성을 찾아서 태그 내용을('오렌지') 출력한다. 
td_list = soup.find('td', {'name':'candy'})
print(td_list.find_next_sibling().string)
 
print ('\n')
 
# 4. 2번과 동일하지만 css selector 방식으로 사용한다.
td_list = soup.select('#choco')
print(td_list[0].string)
 
# 5) 3번과 동일하지만 css selector 방식으로 사용한다.
td_list = soup.select('td[name="candy"]')
print(td_list[0].find_next_sibling().string)
