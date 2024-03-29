# -*- coding: utf-8 -*-
"""# 13398

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rw7nJVYmoa24JHDT4-XkZvWMG9JQHFXv
"""

# 13398 연속합2
n = int(input())
seq = list(map(int, input().split()))

# initalization
dp = [[0 for _ in range(2)] for _ in range(n)]
biggest = seq[0]
dp[0][0] = seq[0]
dp[0][1] = seq[0]

# solution
for i in range(1, n):
    dp[i][0] = seq[i] # 삭제 xx (가장 간단한 연속합 케이스)
    dp[i][1] = seq[i] # 삭제 case 

    dp[i][0] = max(dp[i-1][0] + seq[i], seq[i]) # 삭제 없이 그대로
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + seq[i]) # 삭제하는 경우 vs 삭제한 거 + 합
    biggest = max(biggest, dp[i][0], dp[i][1])

print(biggest)