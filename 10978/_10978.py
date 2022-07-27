# -*- coding: utf-8 -*-
"""# 10978

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IJxwghgQJ_UltsRNHw4zV_1CAmQCOCJB
"""

T = int(input())

dp = [1 for _ in range(21)]
dp[0] = 0

for i in range(2,21):
    dp[i] = i * (dp[i-1] + dp[i-2])

for _ in range(T):
    N = int(input())
    print(dp[N-1])