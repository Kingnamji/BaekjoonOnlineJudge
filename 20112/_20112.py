# -*- coding: utf-8 -*-
"""# 20112

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chicwMKU3SzAB99f4i2j0XwjfyAQ2EOT
"""

# 20112 사토르 마방진

N = int(input())
Sator = [] 
check = True # 사토르 마방진인지 아닌지를 확인해줄 Bool

for i in range(N):
    Sator.append(input())

for i in range(N):
    word = ''
    for j in range(N):
        word += Sator[j][i]
    if word != Sator[i]:
        check = False
        break

if check == False:
    print('NO')
else:
    print('YES')