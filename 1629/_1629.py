# -*- coding: utf-8 -*-
"""# 1629

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P6KOrHIQDQX8BtaaXEzxI4Nj8XfWIKdU
"""

# 1629 곱셈
A, B, C = map(int, input().split())

def sol(A, B, C):
    if B == 1:
        return A%C

    temp = sol(A, B // 2, C)

    if (B%2 == 0):
        return (temp*temp) % C
    else:
        return (temp*temp*A) % C
 
print(sol(A,B,C))