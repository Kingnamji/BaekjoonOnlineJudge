# -*- coding: utf-8 -*-
"""# 1110

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VhrbjancmbYN5VogA60gzX2Qjn0ELryp
"""

# 1110 더하기 사이클

N = int(input())
first = N
count = 0

while 1:
    N = (N%10) * 10 + (N//10 + N%10)%10 
    if N == first:
        count += 1
        break
    else :
        count += 1

print(count)