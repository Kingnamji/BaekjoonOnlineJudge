# -*- coding: utf-8 -*-
"""# 2908

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18st_SRjc2PLyRvGdHfb57ijd_uilSoZa
"""

# 2908 상수
A, B = map(int ,input().split())
A = A//100 + ((A%100)//10) * 10 + (A%10) * 100
B = B//100 + ((B%100)//10) * 10 + (B%10) * 100
if A < B:
    print(B)
else:
    print(A)