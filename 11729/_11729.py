# 11729 하노이 탑 이동 순서
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def hanoi_count(N):
    if N == 1:
        return 1
    else:
        return 2*hanoi_count(N-1) + 1

def hanoi(N, start, to, via):    
    if N == 1:
        print(start, to)
    else:
        hanoi(N-1, start, via, to)
        hanoi(1, start, to, via)
        hanoi(N-1, via, to, start)

print(hanoi_count(N))
hanoi(N, '1', '3', '2')
