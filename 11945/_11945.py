# -*- coding: utf-8 -*-
"""# 11945

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fjCo4zLajgQXRpPmPh72Aq-W-AkP48J3
"""

# 11945 뜨거운 붕어빵
N, M = map(int ,input().split())

bread = []

for i in range(N):
    bread.append(input())

for i in range(N):
    print(bread[i][::-1])