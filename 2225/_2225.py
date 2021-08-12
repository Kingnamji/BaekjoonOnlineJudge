# -*- coding: utf-8 -*-
"""# 2225

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PZOM6BJIT_oAVVW1kGaWilbPsba5X2dn
"""

# 2225 합분해

N, K = map(int, input().split())

dp = [ [0] * (N+1) for i in range(K+1) ]

dp[0][0] = 1

for i in range(1, K+1):
    for j in range(0, N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[K][N])