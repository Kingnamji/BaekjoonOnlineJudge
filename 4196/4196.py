#4196 도미노
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


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    GR = [[] for _ in range(N+1)]
    SCC_idx = [-1 for _ in range(N+1)]
    cnt = 0
    ans = 0
    
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        GR[y].append(x)

    for v in topologicalSort(GR):
        if SCC_idx[v] < 0:
            DFS(v)
            cnt += 1
    
    indegree = [0] * (cnt+1)
    for i in range(1, N+1):
        for w in G[i]:
            if SCC_idx[i] != SCC_idx[w]:
                indegree[SCC_idx[w]] += 1

    for i in range(len(indegree)-1):
        if indegree[i] == 0:
            ans += 1

    print(ans)
