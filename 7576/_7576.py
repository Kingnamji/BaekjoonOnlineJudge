# 7576 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split()) # N => 세로칸 수(row), M = 가로칸 수(col)
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    while queue:
        x, y = queue.popleft() # 토마토 좌표        
        # 익는 토마토 탐색
        for i in range(4):
            new_x, new_y = d[i][0] + x, d[i][1] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if (0<=new_x and new_x<N) and (0<=new_y  and new_y< M) and (not tomato[new_x][new_y]):
                tomato[new_x][new_y] = tomato[x][y] + 1 # 날짜 카운팅
                queue.append((new_x, new_y))

def counting():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not tomato[i][j]:
                return -1
            else:
                cnt = max(cnt, tomato[i][j])
    return cnt-1

# Solution
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

bfs()
print(counting())
