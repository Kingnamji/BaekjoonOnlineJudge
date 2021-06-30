# -*- coding: utf-8 -*-
"""# 1024

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mI4bjurrtPhp7nAbiq7WezSpwRR0tz5H
"""

# 1024 수열의 합
N, L = map(int, input().split())

f = -1
a = 0
x = 0

for i in range(L,101): # 최소 길이인 L 부터 시작
    a = (i * (i-1)) // 2
    if (N-a) % i == 0 and (N-a) // i >= 0: # 음이 아닌 정수 리스트
        f = (N-a) // i
        x = i
        break

if f == -1: # 그런 수열이 없을 때
    print(f)
else:
    for i in range(x):
        print(f+i, end = ' ')