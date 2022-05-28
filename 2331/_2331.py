# -*- coding: utf-8 -*-
"""# 2331

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QExVBv_lBvwPzoLfJhVkavtnzZaiNdZg
"""

# 2331 반복수열
A, P = map(int,input().split())
D = [A]

# 수열의 다음 수 구하는 과정
def Dn(Dn_1, P): 
    sum = 0
    while Dn_1 > 0:
        sum += (Dn_1 % 10) ** P
        Dn_1 = Dn_1 // 10
    
    return sum

# Solution
while True:
    A = Dn(A, P)
    if A in D:
        break
    else:
        D.append(A)

print(D.index(A))