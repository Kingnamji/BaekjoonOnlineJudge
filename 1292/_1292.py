# -*- coding: utf-8 -*-
"""# 1292

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ir0yRBGpCQuL7zmiFLO-fBiWnDI0Tq58
"""

# 1292 쉽게 푸는 문제
number_list = []
num = 0
sum = 0

while  len(number_list) <= 1000:
    num += 1
    for i in range(num):
        number_list.append(num)

number_list = number_list[:1000]
A, B = map(int, input().split())

for i in range(A-1,B):
    sum += number_list[i]

print(sum)