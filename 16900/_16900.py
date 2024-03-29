# -*- coding: utf-8 -*-
"""# 16900

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRSDiwvbT8UTmyCJYj-odERQQQv28SVa
"""

# 16900 이름 정하기

def failure(pattern):
    lenPat = len(pattern)
    tb = [0 for _ in range(lenPat)]
    pidx = 0

    for idx in range(1, lenPat):
        while (pidx > 0 and pattern[pidx] != pattern[idx]):
            pidx = tb[pidx-1]

        if pattern[pidx] == pattern[idx]:
            pidx += 1
            tb[idx] = pidx
    
    return tb

S, K = input().split()
K = int(K)
failureTable = failure(S)
lenS = len(S)

ans = (lenS - failureTable[lenS-1]) * (K-1) + lenS
print(ans)