s1 = "abc" # 줄바꿈 불가능
s2 = 'abc'
s3 = """abc""" # 삼겹따옴표는 줄바꿈 가능 (아래도 동일) 
s4 = '''
강나루 건너서 
밀밭길을
구름에 달 가듯이
가는 나그네
'''
print(s4)
# s2 = 'TOM's Bear'
s2 = "TOM's Bear"
print(s2)
s2 = 'TOM\'s Bear' # 백슬래시는 글자를 묶는 따옴표의 용도를 없애줌
print(s2)
s5 = "홍길동"
s6 = "안녕하세요"
print( s5+s6 )
print( s5+" "+s6 ) # 원래 데이터는 냅두고 공백을 더해주는 게 좋다
# print(s5 + 5) # 오류 (문자와 숫자는 더할 수 없음 + 이후 코드 동작하지 않음) 
print("홍길동 " * 3)
print( "홍길동"[0] ) # 홍
print( "홍길동"[1] ) # 길
print( "홍길동"[2] ) # 동
print( s5[0] ) # 홍
print( s5[1] ) # 길
print( s5[2] ) # 동
print( s5[-1] ) # 동
print( s5[-2] ) # 길
print( s5[-3] ) # 홍
