# -*- coding: utf-8 -*-
"""# 1197

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eFKxUfeOUxMdd1V4ilCYeUHgUDHF2_XY
"""

# 1197 최소 스패닝 트리
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
parent = [0 for _ in range(V+1)] # Union-Find를 위한 부모 노드
edges = [] 
cost = 0 # 가중치 합

for i in range(1, V+1):
    parent[i] = i


# Union-Find
def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


for _ in range(E):
    A, B, weight = map(int,input().split())
    edges.append((weight, A, B))

edges.sort()

for e in edges:
    weight, A, B = e

    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        cost += weight

print(cost)