from collections import deque
import sys

# initialization
N = int(input())

max_size = 128
G = [[0] * max_size for _ in range(max_size)]
adj = [[] for _ in range(max_size)]

for _ in range(N):
    start, end, capa = sys.stdin.readline().rstrip().split()
    start, end, capa = ord(start), ord(end), int(capa)

    G[start][end] += capa
    G[end][start] += capa


# def functions
def bfs(s, t, parent):
    visited = [False] * max_size
    q = deque()

    # initialization
    q.append(s)
    visited[s] = True

    while q:
        start = q.popleft()
        for i, end in enumerate(G[start]):
            if not visited[i] and end > 0:
                q.append(i)
                visited[i] = True
                parent[i] = start

    if visited[t]:
        return True
    else:
        return False
            


def solve(source, sink):
    max_flow = 0
    parent = [-1] * max_size

    while bfs(source, sink, parent):
        now, temp = float('inf'), sink

        while temp != source:
            now = min(now, G[parent[temp]][temp])
            temp = parent[temp]

        max_flow += now

        u = sink
        while u != source:
            v = parent[u]
            G[v][u] -= now
            G[u][v] += now
            u = parent[u]           

    print(max_flow)


solve(ord('A'), ord('Z'))
