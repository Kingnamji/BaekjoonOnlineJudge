# -*- coding: utf-8 -*-
"""# 1085

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IgrDGjkDwdUHv425W7-wF99vsLbyDfgz
"""

# 1085 직사각형에서 탈출
x, y, w, h = map(int, input().split())
a = [x, y, w-x, h-y]

print(min(a))