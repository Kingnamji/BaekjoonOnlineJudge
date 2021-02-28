# -*- coding: utf-8 -*-
"""# 9663

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JGoi4PyaqnXcmcB1epG8b3wDdUM1nV5G
"""

# 9663 N-Queen

n = int(input())
a = [0 for i in range(16)]

ans = 0

def check(x):
    for i in range(1, x):
        if a[x] == a[i] or abs(a[x] - a[i]) == x - i:
            return False
    return True

def DFS(cnt):
    global ans
    if cnt > n:
        ans += 1
    else:
        for i in range(1, n + 1):
            a[cnt] = i
            if check(cnt):
                DFS(cnt + 1)
DFS(1)
print(ans)