# -*- coding: utf-8 -*-
"""# 10867

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fi95yIEPP4vMXmkDKWVFGdK7uQtqdaD-
"""

# 10867 중복 빼고 정렬하기
N = int(input())
nums = list(set(map(int,input().split())))

for i in sorted(nums):
    print(i, end=' ')