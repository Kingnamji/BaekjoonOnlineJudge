# -*- coding: utf-8 -*-
"""# 5622

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mtx17Dkvu3xbBpRuWIFugXTekMjI7rmr
"""

# 5622
word_list = ['ABC',  'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input() # 알파벳 대문자로 이루어진 단어 입력

least_time = 0 # 최소 시간

for i in range(len(word)):
    for j in range(len(word_list)):
        if word[i] in word_list[j]: # 단어 리스트의 j번째에 해당 단어가 속한다면
            least_time += (j+3)

print(least_time)