# -*- coding: utf-8 -*-
"""#1158

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jtAvr4UdWhgW8umuKOpveF898eoujA-Q
"""

# 1158 요세푸스 문제

N, K = map(int, input().split())

num = [i for i in range(1,N+1)] # 1~N이 포함된 리스트
out = [] # 제거된 번호를 넣을 빈 리스트

index = K-1 # 제거할 인덱스 초기값

for i in range(N):
    out.append(num[index]) # 제거된 번호 out에 추가
    num.pop(index) # 제거된 번호 num에서 제거

    if len(num) == 0: # 안하면 error
        break

    index = (index + K - 1) % len(num) 

print('<', end='')
for i in range(N):
    if i == (N-1):
        print(out[i], end='')
    else:
        print(out[i], end=', ')
print('>')