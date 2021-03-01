# -*- coding: utf-8 -*-
"""# 1018

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PgEClYEGAHRJRrne_ZYEga6JFeUK46OF
"""

# 1018 체스판 다시 칠하기
N, M = map(int, input().split())
board = []
new_board = []

for i in range(N): 
    board.append(input())

for j in range(N-7):  # 8*8 로 자를 경우 최대 범위까지 보기위해 -7
    for k in range(M-7):
        start_with_W = 0
        start_with_B = 0
        for s in range(j, j+8): # 8*8 까지 보기위한 이중for문 속의 이중 for문
            for t in range(k, k+8):
                if (s+t) % 2 == 0:
                    if board[s][t] != 'W':
                        start_with_W += 1
                    if board[s][t] != 'B':
                        start_with_B += 1
                else:
                    if board[s][t] != 'B':
                        start_with_W += 1
                    if board[s][t] != 'W':
                        start_with_B += 1   
        new_board.append(start_with_W)
        new_board.append(start_with_B) 

print(min(new_board))