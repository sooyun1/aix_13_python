
from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%84%9C%EC%9A%B8&ackey=0a4fonkc"
target = request.urlopen(url) #접속 정보 등록
soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

tag = "div.detail_info.lv3 > dl" #먼지 오전
dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
dust = ' '.join(dust.split())
print('am dust:', dust)


tag = "div.detail_info.lv2 > dl" #먼지 오후
dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
dust = ' '.join(dust.split())
print('pm dust:', dust)
# dust = soup.select("dd.lvl") #여러개
# print(list(dust))