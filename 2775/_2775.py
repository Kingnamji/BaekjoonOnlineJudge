# -*- coding: utf-8 -*-
"""# 2775

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12HsfqI3Lzxjac7lasc_W6n-OOjprnGK9
"""

# 2775 부녀회장이 될테야
T = int(input())

for i in range(T):
    floor = int(input()) # 층 수 
    n_th = int(input()) # 호 수
    zero_floor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] # 0층의 사람 수수
    for j in range(floor): 
        for k in range(1, n_th):
            zero_floor[k] += zero_floor[k-1]
    print(zero_floor[n_th-1])