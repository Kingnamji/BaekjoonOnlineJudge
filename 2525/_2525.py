# 2525 오븐 시계
A, B = map(int, input().split())
B += int(input())

A += B//60
A %= 24
B %= 60

print(A, B)
