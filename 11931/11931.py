# 11931 수 정렬하기 4
import sys
input = sys.stdin.readline

N = int(input())

ary = []
for _ in range(N):
    ary.append(int(input()))

ary.sort(reverse=True)

for num in ary:
    print(num)
