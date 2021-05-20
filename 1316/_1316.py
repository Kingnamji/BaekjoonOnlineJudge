# -*- coding: utf-8 -*-
"""# 1316

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aXSiOE627TzCUIZau1VoOJFcyrUXA9zO
"""

# 1316 그룹 단어 체커
def is_group(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i] in word[i+1:]:
            return 0
    return 1

N = int(input())
sum = 0

for _ in range(N):
    word = input()
    sum += is_group(word)

print(sum)