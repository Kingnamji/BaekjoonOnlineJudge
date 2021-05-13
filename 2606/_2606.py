# -*- coding: utf-8 -*-
"""# 2606

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iLFNP2jKpGpNs5VKanyoUUdjDNAbaqHj
"""

# 2606 바이러스
import sys
N = int(input()) # 컴퓨터의 수
pair = int(input()) # 쌍의 수
adj = [[0 for _ in range(N)] for _ in range(N)]
visit = [0 for _ in range(N)]
count = 0

def dfs(v):
    visit[v] = 1
    for i in range(N):
        if adj[v][i] == 1 and visit[i] == 0:
            dfs(i)

for _ in range(pair):
    x, y = map(int, sys.stdin.readline().split())
    adj[x-1][y-1] = 1
    adj[y-1][x-1] = 1

dfs(0)

for i in range(1,N):
    if visit[i] == 1:
        count += 1

print(count)