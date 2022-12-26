#2150 SCC
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def topologicalSort(adj):
    def recur(v):
        visited[v] = True

        for i in adj[v]:
            if not visited[i]:
                recur(i)
        ans.append(v)

    ans = []
    visited = [False for _ in range(len(adj))]

    for v in range(1, len(adj)):
        if not visited[v]:
            recur(v)

    ans.reverse()

    return ans

def DFS(v):
    SCC_idx[v] = cnt
    
    for i in G[v]:
        if SCC_idx[i] < 0:
            DFS(i)
            

V, E = map(int, input().split())
G = [[] for _ in range(V+1)] # graph
GR = [[] for _ in range(V+1)] # reverse graph
SCC_idx = [-1 for _ in range(V+1)]
cnt = 0

for _ in range(E):
    A, B = map(int, input().split())
    G[A].append(B)
    GR[B].append(A)

for v in topologicalSort(GR):
    if SCC_idx[v] < 0:
        DFS(v)
        cnt += 1

SCC = [[] for _ in range(cnt)]

for i in range(1, V+1):
    idx = SCC_idx[i]
    SCC[idx].append(i)
    
SCC.sort()
print(cnt)
for i in range(cnt):
    print(*SCC[i], end=" ")
    print(-1)


