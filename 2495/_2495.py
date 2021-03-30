# -*- coding: utf-8 -*-
"""# 2495

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eb0dHwnd4ga6KV9QSfeVPmx2EipyvTbr
"""

# 2495 연속구간

for i in range(3):
    count = 1 # 연속하는 동안 카운트를 해줄 변수
    max_count = 1 # 최대 길이 , 기본값 1
    eight = input()
    start = eight[0]
    for j in eight[1:]:
        if start == j: # 연속한다면
            count += 1 # 카운트 +1
        else: # 연속하지 않으면
            max_count = max(max_count,count) # 현재 가장 긴 count를 저장
            start = j # 해당 숫자부터 다시 start
            count = 1 # 해당 숫자부터 다시 count
    max_count = max(max_count, count) # 마지막 for 문에서 else에 해당하지 않았을 때를 위해 
    print(max_count) # print