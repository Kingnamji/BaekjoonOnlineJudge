# 11051 이항 계수 2
import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

C = factorial(N) // (factorial(K) * factorial(N-K)) # 이항 계수
C %= 10007

print(C)
