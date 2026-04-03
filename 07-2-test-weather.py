from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C%EC%9A%B8&ackey=vf04hyzh"
target = request.urlopen(url) #접속 정보 등록
soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

tag = "div.temperature_text" #온도 (!핵심!)
temp = soup.select_one(tag).get_text() #포함된 모든 글자 추출
print('temp:', temp)
