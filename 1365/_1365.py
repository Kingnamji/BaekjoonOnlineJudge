# -*- coding: utf-8 -*-
"""# 1365

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1usw--JP7UcNEZlfw3G92CAeEjQq7zILv
"""

# 1365 꼬인 전깃줄
N = int(input())
num = list(map(int, input().split()))
lis = [0]

for i in num:
    if lis[-1] < i:
        lis.append(i)
    else:
        start, end = 0, len(lis)
        while start < end:
            mid = (start + end) // 2
            if lis[mid] < i:
                start = mid + 1
            else:
                end = mid
        lis[end] = i

print( N - (len(lis)-1) )