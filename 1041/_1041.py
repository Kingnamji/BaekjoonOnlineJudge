# -*- coding: utf-8 -*-
"""# 1041

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1De7O9U0It_nPAx96SzofLcwk_GHCBvPY
"""

# 1041 주사위
N = int(input())
num = list(map(int, input().split()))

if N == 1:
    print(sum(num) - max(num))
else:
    minList = [ min(num[0], num[5]), min(num[1], num[4]), min(num[2], num[3]) ]
    minList.sort()

    c1 = minList[0]
    c2 = c1 + minList[1]
    c3 = c2 + minList[2]

    ans = c1 * ((N-2)*(N-2) + 4*(N-1)*(N-2)) + c2 * (4*(N-2) + 4*(N-1)) + c3 * 4
    print(ans)