# -*- coding: utf-8 -*-
"""# 11098

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KE-EzR9BSfxqIxznxHkMrzELuXZy9iR3
"""

# 11098 첼시를 도와줘!
import sys
n = int(sys.stdin.readline()) # 테스트 케이스 수

for _ in range(n):
    p = int(sys.stdin.readline()) # 선수의 수
    players = {}

    for _ in range(p): 
        expen = 0
        pay, name = sys.stdin.readline().split()
        players[name] = int(pay)
        
    for player in players:
        if players[player] > expen: expen = players[player]; expen_name = player

    print(expen_name)