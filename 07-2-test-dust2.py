
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus #변환작업

def get_dust(city="서울"):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url) #접속 정보 등록
    soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

    tag = "div.detail_info.lv3 > dl" #먼지 오전
    dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    dust = ' '.join(dust.split())
    dust = dust.split() #공백 제거
    result = {dust[0] : dust[1]} #{오전:나쁨}만 추출
    # print('result am:', result)

    tag = "div.detail_info.lv2 > dl" #먼지 오후
    dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    dust = ' '.join(dust.split())
    dust = dust.split() #공백 제거
    result[dust[0]] = dust[1] #{오후:보통}만 추출, []-> 기존에서 추가
    # print('result:', result)
    return result

get_dust()
# dust = soup.select("dd.lvl") #여러개
# print(list(dust))