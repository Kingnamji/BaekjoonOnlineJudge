# -*- coding: utf-8 -*-
"""# 11720

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y4u39o3gvf995-e8-BT0Psn-qKxRWjNb
"""

# 11720 숫자의 합

N = int(input())
nums = input()
sum = 0

for i in range(N):
    sum += int(nums[i])

print(sum)