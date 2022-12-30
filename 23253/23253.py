# 23253 자료구조는 정말 최고야
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = "Yes"

for _ in range(M):
    k = int(input())
    dummy = list(map(int, input().split()))
    temp = sorted(dummy, reverse=True)

    if dummy != temp:
        ans = "No"

print(ans)
    
    


    
