'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 랜덤으로 10며의 키와 몸무개를 생성하여 파일에 저장
'''
import random

f_name = list('구형김진무한경진여나류')
s_name = list('구형김진무한경진여나류')

with open('body.txt', 'w') as f:
    for i in range(10):
        name = random.choice(f_name) + random.choice(s_name)
        weight = random.randrange(40,100)
        height = random.randrange(140, 195)
        
        f.write("{}, {}, {} \n" .format(name, weight, height))