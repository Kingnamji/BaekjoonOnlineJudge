# 9205 맥주 마시면서 걸어가기
import sys
from collections import deque

def bfs(home_x, home_y, mart, fest_x, fest_y, visited):
    q = deque()
    q.append((home_x, home_y))

    while q:
        x, y = q.popleft()
        if abs(x-fest_x) + abs(y - fest_y) <= 1000:
            return print("happy")
        for i in range(len(mart)):
            if not visited[i]:
                new_x, new_y = mart[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append((new_x, new_y))
                    visited[i] = 1
    return print("sad")


# solution
t = int(sys.stdin.readline()) # 테스트 케이스의 개수

for _ in range(t):
    n = int(sys.stdin.readline()) # 편의점의 개수

    home_x, home_y = map(int, sys.stdin.readline().split()) # 집 좌표
    mart = [] # 편의점 좌표
    for _ in range(n):
        mart_x, mart_y = map(int, sys.stdin.readline().split())
        mart.append( (mart_x, mart_y) )

    fest_x, fest_y = map(int,sys.stdin.readline().split()) # 페스티벌 좌표

    visited = [0 for _ in range(n+1)]
    bfs(home_x, home_y, mart, fest_x, fest_y, visited)
