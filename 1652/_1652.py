# -*- coding: utf-8 -*-
"""# 1652

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zv2B01nzC4VigofNvjEW925J6ZXo4cHI
"""

# 1652 누울 자리를 찾아라
N = int(input())
room = []
x_axis_bed = 0 # x축의 누울 자리 수
count_x = 0 # x축의 .을 셀 변수
y_axis_bed = 0 # y축의 누울 자리 수
count_y = 0 # y의 .을 셀 변수
for i in range(N):
    room.append(input())

for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            count_x += 1
        else :
            if count_x >= 2:
                x_axis_bed += 1
            count_x = 0
    if count_x >= 2:
         x_axis_bed += 1
    count_x = 0

for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            count_y += 1
        else:
            if count_y >= 2:
                y_axis_bed += 1
            count_y = 0
    if count_y >= 2:
        y_axis_bed += 1
    count_y = 0

print(x_axis_bed, y_axis_bed)