# -*- coding: utf-8 -*-
"""# 4796

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17W9npgL5z6x_H4E4EPnf6sR8vOdZtF6D
"""

# 4796 캠핑
import sys
idx = 0
while 1:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
       break

    if V%P < L:
        ans = ((V//P) * L) + (V%P)
    else:
        ans = (V//P) * L + L
        
    idx +=1 
    
    print(f'Case {idx}: {ans}')