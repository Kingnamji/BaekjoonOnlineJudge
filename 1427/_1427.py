# -*- coding: utf-8 -*-
"""# 1427

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uLN6w4mLEuvaFfXzJLJvr7QAQxeB6-C_
"""

# 1427 소트인사이드
N = input() # 문자열로 받는다.
N = sorted(N, reverse=True) # 내림차순으로 정렬

for i in N:
    print(i, end='') # 하나씩 출력