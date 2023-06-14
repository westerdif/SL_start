'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 리스트를 출력하시오
'''
#1~100사이의 정수 중 랜덤으로 10개의 수를 리스트에 저장하시오
import random

num2 = []

for i in range(10):
    num2.append(random.randint(1,100))
print(num2)