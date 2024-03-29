# -*- coding: utf-8 -*-
"""# 14003

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKY71eMGbMbd02GoZH9jnRiqQG_0ENGT
"""

# 14003 가장 긴 증가하는 부분 수열 5
N = int(input())
ary = list(map(int,input().split()))
lis = [-99999999999]
lis_idx = []
ans = []

for i in range(N):
    if lis[-1] < ary[i]:
        lis.append(ary[i])
        lis_idx.append(len(lis))
    else:
        start, end = 0, len(lis)
        while start < end:
            mid = (start+end) // 2
            if lis[mid] < ary[i]:
                start = mid + 1
            else:
                end = mid
        lis[end] = ary[i]
        lis_idx.append(end+1)

lis_len = len(lis)
for i in range(len(lis_idx)-1, -1, -1):
    if lis_idx[i] == lis_len:
        ans.append(ary[i])
        lis_len -= 1
    
    if lis_len == 0:
        break

print(len(ans))
for i in range(len(ans)):
    print(ans[-(i+1)], end = ' ')