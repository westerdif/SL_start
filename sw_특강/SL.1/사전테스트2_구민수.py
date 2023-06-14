'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  자판기 잔돈 계산 프로그램을 작성하시오
        조건: 커피 한잔 가격은 350원 입니다.
        무조건 한 잔만 뽑아 마십니다.
        350원 이하의 동전은 넣지 않습니다.
'''
#돈을 입력하시오(1000원을 넣는것 가정)
money = int(input('돈을 입력하시오 : '))

#커피 한 잔 가격
price = 350

#잔돈을 계산해 변수에 저장
total = money - price

charge = total 

#1000원 갯수
w1000 = charge // 1000
charge = charge % 1000

#500원 갯수
w500 = charge // 500
charge = charge % 500

#100원 갯수
w100 = charge // 100
charge = charge % 100

#50원 갯수
w50 = charge // 50
charge = charge % 50

#잔돈을 출력
print("500원의 갯수는 {}" .format(w500))
print("100원의 갯수는 {}" .format(w100))
print("50원의 갯수는 {}" .format(w50))
print("당신이 받을 잔돈은 {}입니다." .format(total))