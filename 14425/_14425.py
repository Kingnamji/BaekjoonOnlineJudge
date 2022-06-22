# 14425 문자열 집합
import sys
N, M = map(int, sys.stdin.readline().split())
seqN = []
cnt = 0

for _ in range(N):
    seqN.append(sys.stdin.readline().rstrip())

for _ in range(M):
    seq = sys.stdin.readline().rstrip()
    if seq in seqN:
        cnt += 1

print(cnt)
