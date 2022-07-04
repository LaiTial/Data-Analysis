# 조회수 데이터 숫자형으로 변환시키는 함수

def text_to_num(text):
    
    if(text[-2:] == '없음'):
        return 0
    
    #숫자로 변경
    text = text[4:-1]
    
    if(text[-1] == '천'):
        data = float(text[:-1])*1000
    elif(text[-1] == '만'):
        data = float(text[:-1])*10000
    elif(text[-1] == '억'):
        data = float(text[:-1])*100000000
    else:
        data = float(text)
        
    return int(data)
