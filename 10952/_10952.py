# -*- coding: utf-8 -*-
"""#10952

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xcYlI_lpY5dSKjngl0f00x915pYA4FIr
"""

# 10952 A+B -5

while True:
    A, B = map(int,input().split(' ')) # A와 B 입력받기

    if (A == 0) and (B == 0): # 0 두 개가 입력된다면 종료.
        break
    
    print(A+B)