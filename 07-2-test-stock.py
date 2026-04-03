from urllib import request
from bs4 import BeautifulSoup

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
    print('삼성전자 주가', result)

get_stock()

# print('stock:', stock)
print("end")