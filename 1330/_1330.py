# -*- coding: utf-8 -*-
"""#1330

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WP3INRGu8vnpcGOt8mIyF6bjchi68Q99
"""

# 1330 두 수 비교하기

A, B = map(int, input().split(' ')) # 두 정수 A와 B를 입력받는다.

if A == B:
    print("==")
elif A < B:
    print("<")
else:
    print(">")