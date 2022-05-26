# 9251 LCS
import sys
Seq_1 = sys.stdin.readline().rstrip()
Seq_2 = sys.stdin.readline().rstrip()


def lcs(seq_1, seq_2):
    len_1, len_2 = len(seq_1), len(seq_2) # 각 문자열의 길이
    dp = [[0 for _ in range(len_1 + 1)] for _ in range(len_2 + 1)] 

    for i in range(1, len_2 + 1):
        for j in range(1, len_1 + 1):
            if seq_1[j-1] == seq_2[i-1]: # 현재 문자가 같으면 
                dp[i][j] = dp[i-1][j-1] + 1 # 부분 문자열 길이 + 1
            else: # 다르면
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 이전 최댓값

    return dp[len_2][len_1]


print(lcs(Seq_1, Seq_2))
