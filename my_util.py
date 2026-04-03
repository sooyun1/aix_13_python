from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus #변환작업

# 도시이름 입력

# city = "서울"
def get_weather(city="서울"):
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

def get_dust(city="서울"):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url) #접속 정보 등록
    soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

    tag = "div.detail_info.lv2 > dl > dd.lvl" #먼지 오전
    dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    dust = ' '.join(dust.split())
    print('오전 미세먼지는', dust)

    # dust = dust.split() #공백 제거
    # result = {dust[0] : dust[1]} #{오전:나쁨}만 추출
    # print('result am:', result)

    tag = "div.detail_info.lv2 > dl > dd.lvl" #먼지 오후
    dust = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    dust = ' '.join(dust.split())
    print('오후 미세먼지는', dust)

    # dust = dust.split() #공백 제거
    # result[dust[0]] = dust[1] #{오후:보통}만 추출, []-> 기존에서 추가
    # print('result:', result)
    # return result

def get_stock():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80&ackey=azn6ffdn"
    target = request.urlopen(url) #접속 정보 등록
    soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

    tag = "span.spt_con.up > a._target" #온도 (!핵심!)
    stock = soup.select_one(tag).get_text() #포함된 모든 글자 추출
    stock = stock.strip() #앞뒤공백제거
    stock = ' '.join(stock.split()) #모든 공백을 1개로 압축
    stock = stock.split()
    result = {stock[1]} #{오전:나쁨}만 추출
    # print('삼성전자 주가는', result)
    return result

# get_stock()


def get_currency():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8&ackey=0snak8xs"
    target = request.urlopen(url) #접속 정보 등록
    soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

    tag = "span.spt_con.dw > strong" #달러
    money = soup.select_one(tag).get_text() #포함된 모든 글자 추출

    return money



if __name__ == "__main__":
    city = '서울'
    ans = get_weather(city)
    print(f'{city} 습도는 {ans['hum']}')
    ans = get_dust(city)
    # print(f'{city} 오전 미세먼지는 {ans}')
    ans = get_stock()
    print(f'삼성전자 주가는 {list(ans)[0]}')
    print(f'달러 환율은{list(ans)[0]}원')
# print('__name__', __name__)

