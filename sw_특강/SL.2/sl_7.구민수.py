'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 딕셔너리(키와 값으로 이루어짐)
'''
list1 = [[1,'one'], [2, 'two'], [3, 'three']]
dict1 = dict(list1)
print(list1)
print(dict1)

#사전
dict2 = {'제목' : '어벤져스 엔드게임', '장르' : '히어로무비'}
print("영화 : ", dict2)

#특정 키를 지군으로 값을 출력
#키 값과 같은 리스트의 []를 사용
print("movie-name : ", dict2["제목"])
print("movie-tema : ", dict2["장르"])

#영화 감독 이름 추가
print("딕셔너리에 추가")
dict2['감독'] = ['안소니 루소', '조 루소']
print("영화 : ", dict2)

#출연진 추가
dict2['출연진'] = ['아이언맨', '토르', '스칼랫 위치', '소닉', '닥터 스트레인지', '스타로드']
print("영화 : ", dict2)
print("영화 출연진 : ", dict2)

#장르 변경
dict2['장르']  ='SF'
print("영화", dict2)

#다음 코드의 결과를 작성
dict2['출연진'][1] = '타노스'
print("영화 출연진 : ", dict2['출연진'])

print("특별 캐스팅 : ", dict2['출연진'][1])

#출연진 삭제
del dict2['출연진']
print("영화 : ", dict2)

#빈 딕셔너리 생성
student = {}
print("학생 추가 전 : ", student)

student['학과'] = input('학과를 입력하시오 : ')
student['학번'] = input('학번를 입력하시오 : ')
student['이름'] = input('이름를 입력하시오 : ')
print("학새 추가 후 : ", student)

#딕셔너리에 키가 있는지 확인
key  = input("찾고 싶은 키 입력 : ")
if key in student:
    print(student[key])
else:
    print("존재하지 않는 키 입니다.")