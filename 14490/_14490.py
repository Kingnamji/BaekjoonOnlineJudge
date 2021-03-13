# -*- coding: utf-8 -*-
"""# 14490

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rtf6fxr9ihLmRxCWPZGuraaG5-H1rADf
"""

# 14490 백대열
n,m = map(int, input().split(':'))

def gcd(n,m):
    if n < m:
        temp = n
        n = m
        m = temp
    while m != 0:
        r = n % m
        n = m
        m = r
    return n

gcd = gcd(n,m)
div_n = int(n / gcd)
div_m = int(m / gcd)

print(f'{div_n}:{div_m}')