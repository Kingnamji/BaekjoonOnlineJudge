# -*- coding: utf-8 -*-
"""#2739

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12a1IWYBZvTAs7YSRu5ePo4PQju2QjqBr
"""

# 2739 구구단

N = int(input()) # N단을 입력받는다


for i in range(9):
    print(f'{N} * {i+1} = {N * (i+1)}') # f-string 문자열 포매팅