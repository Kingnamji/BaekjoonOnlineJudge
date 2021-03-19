# -*- coding: utf-8 -*-
"""# 11653

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jcz8CeC4jnFLEw-D7XYGqSAIUC6kWZx9
"""

# 11653 소인수분해
N = int(input())
div = 2

while N != 1: # 입력이 1이면 아무 것도 출력하지 않는다.
    if div > N ** 0.5: # N의 제곱근보다 나눌 수가 커진다면 N은 반드시 소수가 된다.
        print(N) # 남은 N만 출력
        break # 프로그램 종료
    if N % div == 0: # div 로 나눠진다면
        N = N//div
        print(div)
    else:
        div += 1 # 나눌 수를 +1