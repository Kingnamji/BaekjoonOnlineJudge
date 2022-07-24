# -*- coding: utf-8 -*-
"""# 22945

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YWZI3cpVjbHGjCVP9CnVbCtSjAtdKEPJ
"""

# 22945 팀 빌딩
N = int(input())
seq = list(map(int, input().split()))

ans = 0
left, right = 0, N-1

while left <= right:
    ans = max(ans, (right-left-1) * min(seq[left], seq[right]))

    if seq[left] <= seq[right]:
        left += 1
    else:
        right -= 1

print(ans)