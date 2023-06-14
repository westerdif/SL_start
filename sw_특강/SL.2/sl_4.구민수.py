'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : list.continue
'''
#리스트의 값이 10개 중에서 10보다 큰 수를 출력하시오
numbers = [1,12,23,34,45,56,67,78,89,10]

print("리스트 값 중 10보다 큰 수 - 반복문 사용")

for i in numbers:
    if i >= 10:
        print(i, end=', ')
        

print("리스트 값 중 10보다 큰 수 - continue 사용")

for i in numbers:
    if i <= 10:
        continue
    print(i, end=', ')
    

print()

#1~30 사이의 수 중에서 7의 배수만 출력하시오. - continue
numbers_2 = []
num = 1

for i in range(1, 31):
    numbers_2.append(num)
    num = num +1
    
print("1~30사이의 수")
print(numbers_2)

for i in numbers_2:
    if i % 7 != 0:
        continue
    print(i, end=', ')

print()