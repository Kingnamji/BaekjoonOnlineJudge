# -*- coding: utf-8 -*-
"""# 1437

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TTcCZ2NRh-OzcppMxGaL_FUwdZ2M3K_M
"""

# 1437 수 분해

N = int(input())
dp = [i for i in range(1000001)]
dp[0] = 0

for i in range(5, len(dp)):
    dp[i] = (dp[i-3]*3)%10007

print(dp[N])