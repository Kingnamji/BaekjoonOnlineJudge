# -*- coding: utf-8 -*-
"""# 2417

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E2DvFjOfbcpyh_FnCz36IaMeZAgxmBz3
"""

# 2417 정수 제곱근

N = int(input())

square_N = N**0.5

if square_N % 1 == 0:
    print(int(square_N))
else:
    print(int(square_N) + 1)