# -*- coding: utf-8 -*-
"""# 10830

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rKUaHlYqJdhmIhvUmTsAnqUj2vGrZlX_
"""

# 10830 행렬 제곱
import sys

def multiple(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif B%2 == 0: # 나눠지면 분할해서 푸는게 더 좋음
        temp = [[0 for _ in range(N)] for _ in range(N)]
        recursive = multiple(A, B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += recursive[i][k] * recursive[k][j]
                temp[i][j] %= 1000
        return temp
    else:
        temp = [[0 for _ in range(N)] for _ in range(N)]
        recursive = multiple(A, B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][j] += recursive[i][k] * A[k][j]
                temp[i][j] %= 1000
        return temp

N, B = map(int, input().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range (N)]# 행렬

ans = multiple(A,B)

# 행 별로 원소 출력
for i in ans: 
    for j in i:
        print(j, end = ' ') # 
    print()