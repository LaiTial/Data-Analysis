# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:59:56 2022

@author: asna9
읽어서 저장한 벅스뮤직 top100 파일을 읽는다.
"""

try:
    file = open('bugs100.txt', 'r', -1, 'UTF-8')
    
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("bugs100.txt 파일이 디스크에 없습니다.")