# -*- coding: utf-8 -*-
"""# 2839

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11JNwjEALO8C0cNQqI7qkKmvB-VhInH5r
"""

# 2839 설탕 배달

N = int(input())
count = 0

while (N > 0):
    if (N % 5) == 0:
        N -= 5
        count += 1
    elif (N % 3) == 0:
        N -= 3
        count += 1
    elif (N > 5):
        N -= 5
        count += 1
    else:
        count = -1
        break
    
print(count)