'''
작성일 : 2023년 00월 00일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 비만도 계산
'''
with open('body.txt', 'r') as f:
    for i in f:
        (name, weight, height) = i.strip().split(", ")
        
        if (not name) or (not weight) or (not height) :
            continue
        
        bmi = int(weight) / ((int(height) / 100) ** 2)
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상체중"
        else:
            result = "저체중"
        
        print("\n" .join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {:.2f}", "결과 : {}"]) .format(name, weight, height, bmi, result))