# 1914 하노이 탑
import sys
sys.setrecursionlimit(10 ** 6)

def hanoi_counting(N):
    if N == 1:
        return 1
    else:
        return 2*hanoi_counting(N-1) + 1

def hanoi(N, start, to, via):
    if N == 1:
        print(start, to)
    else:
        hanoi(N-1, start, via, to)
        hanoi(1, start, to, via)
        hanoi(N-1, via, to, start)

N = int(input())
print(hanoi_counting(N))

if N <= 20:
    hanoi(N, '1', '3', '2')
