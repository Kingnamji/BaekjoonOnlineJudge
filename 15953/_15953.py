# -*- coding: utf-8 -*-
"""# 15953

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XDCKuiRvCmRl8ggbNMgKyJQHOGXJGVXk
"""

# 15953 상금 헌터

first = [500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
second = [512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    money = 0

    if a == 0 or a > 21: # 본선에 진출하지 못했거나, 순위권 밖
        pass
    else:
        money += first[a-1]

    if b == 0 or b > 31: # 본선에 진출하지 못했거나, 순위권 밖
        pass
    else:
        money += second[b-1]

    print(money * 10000)