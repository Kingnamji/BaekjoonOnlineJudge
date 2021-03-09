# -*- coding: utf-8 -*-
"""# 20159

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nMIEFN46pmclN2AGZ04SEx10NFYB8LAL
"""

# 20159 동작 그만. 밑장 뺴기냐?
N = int(input())
card_list = list(map(int, input().split()))
start_second = sum(card_list[1::2]) # 상대가 원래 받는 합

ans = start_second

sum = card_list[0] # 첫번째 카드부터 더하기 (플레이어 먼저 시작)
temp = 0
for i in range(1, len(card_list)):
    if i % 2: # 홀수번째
        temp = sum + start_second - card_list[-1]
        start_second -= card_list[i]
    else:  # 짝수번째
        temp = sum + start_second
        sum += card_list[i]

    if temp > ans:
        ans = temp

print(ans)