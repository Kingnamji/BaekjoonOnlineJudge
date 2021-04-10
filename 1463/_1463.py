# -*- coding: utf-8 -*-
"""# 1463

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gUtMRrZA9bCAKPUQqdfMjbgiUUrtOzjE
"""

# 1463 1로 만들기
N = int(input())

ops = [0 for _ in range(N+1)] # 연산 횟수

for i in range(2, N+1):
    ops[i] = ops[i-1] + 1

    if (i%2 == 0) and ops[i] > ops[i//2] + 1:
        ops[i] = ops[i//2] + 1
    
    if (i%3 == 0) and ops[i] > ops[i//3] + 1:
        ops[i] = ops[i//3] + 1
        
print(ops[N])