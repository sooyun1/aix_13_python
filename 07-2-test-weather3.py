from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus #변환작업

# 도시이름 입력

city = "서울"
def get_weather(city):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
    target = request.urlopen(url) #접속 정보 등록
    soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

    tag = "div.temperature_text" #온도 (!핵심!)
    mytemp = soup.select_one(tag).get_text().strip() #포함된 모든 글자 추출 +공백제거

    tag = "div.temperature_info" #습도, 날씨, 풍량 정보
    temp = soup.select_one(tag).get_text() #포함된 모든 글자 추출, 공백이 많아짐
    temp = temp.strip() #앞뒤공백제거
    temp = ' '.join(temp.split()) #모든 공백을 1개로 압축
    temp = temp.split()

    return {
        'temp':mytemp,
        'yestd':temp[1]+" "+temp[2], #어제보다 몇도
        'weather':temp[3], #날씨
        'hum':temp[7], #습도
        'windd':temp[8], #풍향
        'winds':temp[9], #풍속
    }

city = '서울'
ans = get_weather(city)
print(f'{city} 온도는 {ans}')