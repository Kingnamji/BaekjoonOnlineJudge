# -*- coding: utf-8 -*-
"""# 14487

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1--AF57UMC7-_O4u2vrFvoggkpQjO3ZI8
"""

# 14487 욱제는 효도쟁이야!!
N = int(input())
cost_list = list(map(int ,input().split()))
# 원 모양을 다 돌아야한다. 이동거리가 제일 큰 구간을 빼고 돌면 된다.
print( sum(cost_list) - max(cost_list) )