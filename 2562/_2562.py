# -*- coding: utf-8 -*-
"""#2562

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BCsbgHab6zidem5JtEyRr4PdBI4jvHcc
"""

# 2562 최댓값

max = 0 # 입력이 자연수이기 때문에 최댓값의 초기값은 0으로 설정

for i in range(9):
    num = int(input())
    
    if max < num :
        max = num
        idx = i+1

print(max)
print(idx)