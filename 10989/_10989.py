# -*- coding: utf-8 -*-
"""# 10989

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ylPcWyi7z3vzIohAkXJo8OUIqsU6aKC5
"""

# 10989 수 정렬하기 3 
# 카운팅을 해줄 리스트를 만들어서 풀면 된다.
import sys
N = int(sys.stdin.readline())

cnt = [0 for i in range(10001)]

for i in range(N):
    cnt[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(cnt[i]):
        print(i)