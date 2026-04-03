from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus #변환작업

city = input("날씨를 알고 싶은 도시 이름 입력>> ")
city = quote_plus(city)

url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
target = request.urlopen(url)
soup = BeautifulSoup(target, 'html.parser')

temp = soup.select_one("div.temperature_text").get_text()
print('temp=', temp)
hum = soup.select_one("dl.summary_list").get_text()
# print('습도=', hum)
a = hum.strip().split(' ')
print('습도=', a[5])

print('end')