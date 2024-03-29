# -*- coding: utf-8 -*-
"""# 1932

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k1iC88BsHbLcT4dBMQlm69cdjbF8f3iu
"""

# 1932 정수 삼각형
import sys
n = int(input())
ints = []

for _ in range(n):
    nodes = list(map(int, sys.stdin.readline().split()))
    ints.append(nodes)

for i in range(1,n):
    length = len(ints[i])
    for j in range(length):
        if j == 0:
            ints[i][j] += ints[i-1][j]
        elif j == (length - 1):
            ints[i][j] += ints[i-1][j-1]
        else:
            ints[i][j] += max(ints[i-1][j-1], ints[i-1][j])

print(max(ints[n-1]))