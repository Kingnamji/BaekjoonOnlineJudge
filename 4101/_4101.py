# -*- coding: utf-8 -*-
"""# 4101

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KYkgTwQt2lKIQwYLjf76HYiA04JfD8gt
"""

# 4101 크냐?
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break

    if a > b:
        print('Yes')
    else:
        print('No')