from urllib import request
from bs4 import BeautifulSoup


# def get_currency("달러"):
#     url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8&ackey=0snak8xs"
#     target = request.urlopen(url) #접속 정보 등록
#     soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

#     tag = "span.spt_con.dw > strong" #달러
#     money = soup.select_one(tag).get_text() #포함된 모든 글자 추출
#     print('money:', money)

# get_currency("달러")

# ans = get_currency("달러")
# print(ans)
# return money

# money = get_currency()

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8&ackey=0snak8xs"
target = request.urlopen(url) #접속 정보 등록
soup = BeautifulSoup(target, "html.parser") #구조 분해 분석

tag = "span.spt_con.dw > strong" #달러
money = soup.select_one(tag).get_text() #포함된 모든 글자 추출
print('money:', money+"원")
