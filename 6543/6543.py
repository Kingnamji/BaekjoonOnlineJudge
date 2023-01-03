# 6543 그래프의 싱크
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def topologicalSort(adj):
    def recur(v):
        visited[v] = True

        for w in adj[v]:
            if not visited[w]:
                recur(w)
        ans.append(v)


    visited = [False for _ in range(len(adj))]
    ans = []

    for v in range(1, len(adj)):
        if not visited[v]:
            recur(v)
            
    ans.reverse()

    return ans
    

def sol():
    def DFS(v):
        SCC_idx[v] = idx
        for w in G[v]:
            if SCC_idx[w] < 0:
                DFS(w)

    while True:
        inputs = list(map(int, input().split()))
        
        if inputs[0] == 0:
            break

        n, m = inputs[0], inputs[1]

        edges = list(map(int, input().split()))
        G = [[] for _ in range(n+1)]
        GR = [[] for _ in range(n+1)]
        
        for i in range(m):
            v_idx, w_idx = edges[i*2], edges[i*2+1]
            G[v_idx].append(w_idx)
            GR[w_idx].append(v_idx)

        SCC_idx = [-1 for _ in range(n+1)]
        idx = 0
        for v in topologicalSort(GR):
            if SCC_idx[v] < 0:
                DFS(v)
                idx += 1

        out = [0] * idx
        for v in range(1, n+1):
            for w in G[v]:
                if SCC_idx[v] != SCC_idx[w]: # 두 정점이 속하는 SCC가 다름
                    out[SCC_idx[v]] += 1 # 나가는 간선 수 += 1

        sink = []
        for v in range(1, n+1):
            if not out[SCC_idx[v]]:
                sink.append(v)

        print(*sink)
        
sol()  
