# -*- coding: utf-8 -*-
"""# 1940

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y-uxngLRJwXHx0BY3h9YcDxl5PEgYLT9
"""

# 1940 주몽
N = int(input())
M = int(input())
ary = list(map(int, input().split()))

ary.sort()
cnt = 0

i = 0
j = N-1
while i<j:
    if ary[i] + ary[j] == M:
        i += 1
        j -= 1
        cnt += 1
    elif ary[i] + ary[j] < M:
        i += 1
    else:
        j -= 1

print(cnt)