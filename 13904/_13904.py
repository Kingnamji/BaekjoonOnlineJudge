# -*- coding: utf-8 -*-
"""# 13904

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVzZR88eDT4BVKjC7f8VTXEZm0VpV12q
"""

# 13904 과제
N = int(input())
hw = []

for _ in range(N):
    d, w = map(int, input().split()) # d: 과제 마감일 까지 남은 일, w: 과제의 점수
    hw.append((d,w))

hw.sort(reverse=True, key=lambda x:x[1])

score = [0 for _ in range(1001)] # 점수 저장

for i in range(N):
    temp = hw[i][0] # 남은 일자
    
    while temp: # 최대한 늦게 하도록
        if score[temp] == 0: # 점수 저장(이미 높은 순)
            score[temp] = hw[i][1] 
            break # 최대한 늦게 저장해놓고 break
        temp -= 1
    
print(sum(score))