# -*- coding: utf-8 -*-
"""# 11134

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JXBdjvdW5QCFv51Snt6dg6g-odCa1mj0
"""

# 11134 쿠키애호가
import sys
T = int(input())

for _ in range(T):
    N, C = map(int, sys.stdin.readline().split())
    
    if N%C:
        print(N//C+1)
    else:
        print(N//C)