from urllib import request
from bs4 import BeautifulSoup


url = "https://news.naver.com/section/105"
target = request.urlopen(url) #접속 정보 등록
soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

tag = "li.rl_item .rl_txt" #신문기사 제목
news = soup.select(tag) #태그 하나에 포함된 모든 글자 추출
for t in news:
    title = t.get_text()
    print('기사제목', title)
    # stock = stock.strip() #앞뒤공백제거
    # stock = ' '.join(stock.split()) #모든 공백을 1개로 압축
    # stock = stock.split()
    # result = {stock[1]} #{오전:나쁨}만 추출

# get_stock()

# print('stock:', stock)