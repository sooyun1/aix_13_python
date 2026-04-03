# m1 = {"name":"어벤저스 엔드게임","type":"히어로 무비"}
# print(m1)
# # 학생정보
# st1 = {"name":"홍길동","hakbun":1120}
# print(st1['name']) # 홍길동
# print(st1['hakbun']) # 1120
# scoreDict = {
#     "홍길동":[80,70,90],
#     "김길동":[60,70,80],
#             }
# print(scoreDict['홍길동'])
# # 문제발생. 홍길동의 수학점수를 알 수 없음
# # 구조변경

# scoreDict = {
#     "홍길동":{"guk":80,"math":70,"eng":90},
#     "김길동":{"guk":70,"math":60,"eng":80}
#             }
# print("홍길동의 수학점수",scoreDict["홍길동"]["guk"]) 
# # 사이에 쉼표 넣으면 홍길동의 점수들과 "guk"만 뜸. 주의
# print("홍길동의 국어점수",scoreDict["홍길동"]["guk"], "김길동의 수학점수", scoreDict["김길동"]["math"]) 

# n = "홍길동"
# # 키는 immutable Object만 가능. 불변객체(한 번 값을 정하면 중간에 수정, 삭제 기능이 안 되는 )
# dic1 = {
#     n : 90
# }
# print(dic1)

# dict2 = {
#     (1,3): 90 # 튜플
# }

dict3 = dict() # 빈 사전 생성
print(dict3)
dict3["a"] = 70
dict3["b"] = 80
print(dict3)
dict3["a"] = 100 # 덮어씀
print(dict3)
del dict3['a']
print('삭제 후',dict3)
# del dict3['a'] # error. 이미 없어진 걸 또 삭제할 순 없음
# 학생 점수 관리
# scores = dict()
# scores["홍길동"] = {
#     'guk':70, 'math':80, 'eng':70
#     }
# scores["박길동"] = {
#     'guk':80, 'math':90, 'eng':70
#     }
# name = input('학생이름>> ')
# # if name in scores:
# #     print(f'{name}의 점수 {scores[name]}')
# # else:
# #     print(f'{name}은 미등록 학생')
# value = scores.get(name)
# if value == None:
#     print(f'{name}은 미등록 학생')
# else:
#     print(f'{name}의 점수 {scores[name]}')

scores2 = {
    "홍":70, "김":80, "강":75, "권":90
}
for k in scores2:
    print(f'{k} {scores2[k]}')
