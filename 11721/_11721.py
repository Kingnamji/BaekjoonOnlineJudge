# -*- coding: utf-8 -*-
"""# 11721

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zq2cc_8jageeP2Um2W4gqfKxNg_kpv-y
"""

# 11721 열 개씩 끊어 출력하기
N = input()

for i in range(0,len(N),10):
    print(N[i:i+10])