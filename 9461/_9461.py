# -*- coding: utf-8 -*-
"""# 9461

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oDrq5ErUnR09m_gjJn0PTnIHma5c_kwM
"""

# 9461 파도반 수열
import sys
T = int(input())
dp = [1 for _ in range(101)]

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])