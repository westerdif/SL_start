'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 학생 정보를 딕셔너리에 저장하고
       특정 학생의 정보(학번)을 입력하여 학생을 찾아주세요
       
       (학생, 학번, 이름, 전화번호)
'''
###알고리즘###
#학생 정보 저장
#학생 정보 입력 - 사전에 저장(Z를 누르면)
#학번으로 검색하기 - 무한반복(학번이 빈칸이면 검색 종료)

student_info = {}

print("===학생 정보 입력===")
while True:
    student = {}
    student['학과'] = input('학과를 입력하시오 : ')
    if student['학과'] == 'Z':
        break
    student['학번'] = input('학번를 입력하시오 : ')
    if student['학번'] == 'Z':
        break
    student['이름'] = input('이름를 입력하시오 : ')
    if student['이름'] == 'Z':
        break
    student['전화번호'] = input('전화번호를 입력하시오 : ')
    if student['전화번호'] == 'Z':
        break
    
    student_info[student['학번']] = student
    
print(student_info)

print("===학생 정보 출력===")
while True:
    number = input('찾으실 학번 입력 : ')
    if number == ' ':
        break
    else:
        print("학생 정보 출력 : ", student_info.get(number))
