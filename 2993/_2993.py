# -*- coding: utf-8 -*-
"""# 2993

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8_4J544TwtVBHgIwiEwLJRnKM729gMj
"""

# 2993 세 부분
word = input()
words = []

for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            new = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            words.append(new)

print(min(words))