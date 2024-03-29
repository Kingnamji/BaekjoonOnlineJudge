# -*- coding: utf-8 -*-
"""# 1259

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPqaHOX0zL_FE2vQjMNqxpeZrTl-2w-Z
"""

# 1259 팰린드롬수
import sys
def palindrome(seq):
    N = len(seq)
    
    for i in range(N//2):
        if seq[i] != seq[-(i+1)]:
            return False
    return True

while 1:
    num = sys.stdin.readline().rstrip()
    
    if num == '0':
        break
    
    if palindrome(num):
        print('yes')
    else:
        print('no')