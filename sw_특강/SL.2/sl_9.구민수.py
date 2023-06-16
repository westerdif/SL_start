'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 사용자로부터 점수를 입력 받아 1부터 입력받은 수 까지
       369게임을 진행합니다.
       3,6,9에서는 '짝'을 
       10,20,30... 10의 배수 자리에는 '만세'를 출력하는 부분은  함수로 작성하시오
'''
def tsn_game(num):
    for i in range(num+1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝", end=', ')
        elif i % 10 == 0:
            print("만세", end=', ')
        else:
            print(i, end=', ')

print("3,6,9 게임")
num = int(input("수를 입력하시오 : "))
tsn_game(num)