# -*- coding: utf-8 -*-
"""# 11966

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUgXAZ3l19DQGtGxUDi_LvMLCnu3zvEs
"""

# 11966 2의 제곱인가?

N = int(input())
check_list = []

for i in range(31):
    check_list.append(2 ** i)

if N in check_list:
    print(1)
else:
    print(0)