# -*- coding: utf-8 -*-
"""# 11656

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZ7ajyJgpV4o6ZhwVfGUaDnJBxCbX9H7
"""

# 11656 접미사 배열

S = input()
ary = [] # 접미사 배열

length = len(S)

for i in range(length):
    ary.append(S[i:])

ary.sort() # 사전순으로 정렬

for word in ary:
    print(word)