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
    temp = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    return temp

city = '부산'
ans = get_weather(city)
print(f'{city} 온도는 {ans}')

