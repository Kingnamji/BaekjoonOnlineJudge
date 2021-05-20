# -*- coding: utf-8 -*-
"""# 1453

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vVJR4ZJVe1S8Sh2a7qq7dc25KahV7Agu
"""

# 1453 피시방 알바

N = int(input()) # 손님의 수
nums = map(int, input().split())
seats = [0 for _ in range(101)] # 자리

refuse = 0 # 거절당한 횟수

for i in nums:
    if seats[i] == 0: # 예약한 사람이 없다 
        seats[i] = 1 # 예약
    else: # 이미 예약된 자리
        refuse += 1 # 거절

print(refuse)