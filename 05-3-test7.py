with open("info.txt","r",encoding='utf8') as file: #유니코드:utf8 (변환)
    for line in file: #한줄씩 읽음
        name,w,h = line.strip().split(',') #리스트 형태
        bmi = int(w) / int(h)*int(h)
        result = ""
        if 25 <= bmi:
            result='과체중'
        elif 18.5 <= bmi:
            result='정상체중'
        else:
            result='저체중'
        print(f'이름:{name} 몸무게:{w} 키:{h}')
        print(f'BMI:{round(bmi)} 결과:{result}') #결과값이 너무 길어지니 반올림
        