'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 ㅣ파일 입출력
설명 : 학생의 이름과 점수를 입력받아 리스트에 저장하고,
       학생 점수의 총점과 평균을 입력하시오
'''
###알고리즘###
#빈 학생 리스트 생성
#학생 수 입력 받기 
#학생 수 만큼 반복하면서
    #학생의 이름과 점수 저장 - 리스트
    #점수 합계 계산
#리스트에 저장된 학생 정보 출력
#총점과 평균 출력

students = []
sum = 0

num = int(input('학생 수를 입력하시오: '))

for i in range(num):
    print("<", i+1, "번째 학생 정보 출력")
    name = input('학생 이름 입력 : ')
    score = int(input("%s의 점수 입력 : " %name))
    students.append([name, score])
    sum = sum + score
    
for info in students:
    print("이름 : ", info[0], "점수 : ", info[1])
    
print("학생 점수의 합계 : " .format(sum))
print("학생 점수 평균 : {:.2f}" .format(sum/num))
    