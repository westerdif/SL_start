'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 ㅣ파일 입출력
설명 : 
'''
students = []

while True:
    num = int(input("작업 선택 : "))
    
    if num == 0:
        break
    
    elif num == 1:
        print(students)
        
    elif num == 2:
        students.append(input("추가할 학생 이름 : "))
    
    elif num == 3:
        del_student = input("삭제할 학생의 이름을 입력하시오: ")
        if del_student in students:
            students.remove(del_student)
        else:
            print("삭제할 학생이 없습니다.")
            
print("학생 조회 {}:" .format(students))
print("학생 추가 {}:" .format(students))
print("학생 삭제 {}:" .format(students))