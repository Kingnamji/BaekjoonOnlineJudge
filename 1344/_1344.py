# -*- coding: utf-8 -*-
"""# 1344

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X79oKvrCgD-PvQv6r0bD4dRZJb0RacKP
"""

# 1344 폴리오미노
seq = input()

seq = seq.replace("XXXX", "AAAA")
seq = seq.replace("XX", "BB")

if 'X' in seq:
    print(-1)
else:
    print(seq)