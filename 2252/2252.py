#2252 줄 세우기
import sys
input = sys.stdin.readline

def topologicalSort(adj):
    def recur(v):
        visited[v] = True
        for i in (adj[v]):
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
        

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)

ans = topologicalSort(adj)

for i in ans:
    print(i, end = " ")
