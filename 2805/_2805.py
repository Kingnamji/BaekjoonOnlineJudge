# -*- coding: utf-8 -*-
"""# 2805

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tg36Frq16ejdhC5fQ2eyYqGY3v1p-LEH
"""

# 2805 나무 자르기

N, M = map(int, input().split())
woods = list(map(int, input().split()))
start = 1
H = max(woods) # 절단기의 높이

while start <= H: # 이분 탐색
    mid = (start + H) // 2
    sum_woods = 0 # 벌목한 나무 길이의 총 합

    for i in woods:
        if i > mid:
            sum_woods += i-mid

    if sum_woods >= M:
        start = mid + 1
    else:
        H = mid - 1

print(H)